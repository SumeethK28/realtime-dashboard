// Chart configurations
const chartConfigs = {
    tempStock: null,
    server: null,
    revenue: null,
    social: null,
    weather: null,
    traffic: null
};

// Initialize all charts
function initializeCharts() {
    // Temperature & Stock Chart (Dual Axis)
    const tempStockCtx = document.getElementById('tempStockChart').getContext('2d');
    chartConfigs.tempStock = new Chart(tempStockCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'Temperature (°C)',
                    data: [],
                    borderColor: '#FF6384',
                    backgroundColor: 'rgba(255, 99, 132, 0.1)',
                    yAxisID: 'y',
                    tension: 0.4
                },
                {
                    label: 'Stock Price ($)',
                    data: [],
                    borderColor: '#36A2EB',
                    backgroundColor: 'rgba(54, 162, 235, 0.1)',
                    yAxisID: 'y1',
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { type: 'linear', position: 'left', title: { display: true, text: 'Temperature (°C)' } },
                y1: { type: 'linear', position: 'right', title: { display: true, text: 'Stock Price ($)' }, grid: { drawOnChartArea: false } }
            }
        }
    });

    // Server Metrics Chart
    const serverCtx = document.getElementById('serverChart').getContext('2d');
    chartConfigs.server = new Chart(serverCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                { label: 'CPU %', data: [], borderColor: '#FF6384', tension: 0.4 },
                { label: 'Memory %', data: [], borderColor: '#36A2EB', tension: 0.4 },
                { label: 'Disk %', data: [], borderColor: '#FFCE56', tension: 0.4 }
            ]
        },
        options: { responsive: true, maintainAspectRatio: false }
    });

    // Revenue Chart (Bar)
    const revenueCtx = document.getElementById('revenueChart').getContext('2d');
    chartConfigs.revenue = new Chart(revenueCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Revenue ($)',
                data: [],
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
            }]
        },
        options: { responsive: true, maintainAspectRatio: false }
    });

    // Social Media Chart (Radar)
    const socialCtx = document.getElementById('socialChart').getContext('2d');
    chartConfigs.social = new Chart(socialCtx, {
        type: 'radar',
        data: {
            labels: [],
            datasets: [{
                label: 'Engagement Rate (%)',
                data: [],
                backgroundColor: 'rgba(102, 126, 234, 0.2)',
                borderColor: '#667eea',
                pointBackgroundColor: '#667eea'
            }]
        },
        options: { responsive: true, maintainAspectRatio: false }
    });

    // Weather Chart (Bar)
    const weatherCtx = document.getElementById('weatherChart').getContext('2d');
    chartConfigs.weather = new Chart(weatherCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Temperature (°C)',
                data: [],
                backgroundColor: '#36A2EB'
            }]
        },
        options: { responsive: true, maintainAspectRatio: false }
    });

    // Traffic Chart (Horizontal Bar)
    const trafficCtx = document.getElementById('trafficChart').getContext('2d');
    chartConfigs.traffic = new Chart(trafficCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Vehicle Count',
                data: [],
                backgroundColor: '#FF6384'
            }]
        },
        options: { 
            responsive: true, 
            maintainAspectRatio: false,
            indexAxis: 'y'
        }
    });
}

// Fetch and update all data
async function fetchAllData() {
    try {
        const response = await fetch('/api/all-data/');
        const data = await response.json();
        
        // Update stats
        updateStats(data);
        
        // Update charts
        updateCharts(data);
        
        // Update tables
        updateTables(data);
        
        // Fetch analytics
        await fetchAnalytics();
        
        // Update last update time
        document.getElementById('lastUpdate').textContent = 
            'Last updated: ' + new Date().toLocaleTimeString();
        
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function updateStats(data) {
    // Average Temperature
    if (data.sensors.length > 0) {
        const avgTemp = data.sensors.reduce((sum, s) => sum + s.temperature, 0) / data.sensors.length;
        document.getElementById('avg-temp').textContent = avgTemp.toFixed(1) + '°C';
    }
    
    // CPU Usage (latest)
    if (data.system_metrics.length > 0) {
        const latestCPU = data.system_metrics[0].cpu_usage;
        document.getElementById('cpu-usage').textContent = latestCPU.toFixed(1) + '%';
    }
    
    // Average Stock Price
    if (data.stocks.length > 0) {
        const avgStock = data.stocks.reduce((sum, s) => sum + s.price, 0) / data.stocks.length;
        document.getElementById('avg-stock').textContent = '$' + avgStock.toFixed(2);
    }
    
    // Total Revenue
    if (data.ecommerce.length > 0) {
        const totalRevenue = data.ecommerce.reduce((sum, t) => sum + t.amount, 0);
        document.getElementById('total-revenue').textContent = '$' + totalRevenue.toFixed(2);
    }
    
    // Social Media Engagement
    if (data.social_media.length > 0) {
        const totalEngagement = data.social_media.reduce((sum, s) => sum + s.likes + s.shares + s.comments, 0);
        document.getElementById('social-engagement').textContent = totalEngagement.toLocaleString();
    }
    
    // Traffic Average
    if (data.traffic.length > 0) {
        const avgVehicles = data.traffic.reduce((sum, t) => sum + t.vehicle_count, 0) / data.traffic.length;
        document.getElementById('traffic-vehicles').textContent = Math.round(avgVehicles);
    }
}

function updateCharts(data) {
    // Temp & Stock Chart
    if (data.sensors.length > 0 && data.stocks.length > 0) {
        const tempData = data.sensors.slice(0, 15).reverse();
        const stockData = data.stocks.slice(0, 15).reverse();
        
        chartConfigs.tempStock.data.labels = tempData.map(d => new Date(d.timestamp).toLocaleTimeString());
        chartConfigs.tempStock.data.datasets[0].data = tempData.map(d => d.temperature);
        chartConfigs.tempStock.data.datasets[1].data = stockData.map(d => d.price);
        chartConfigs.tempStock.update('none');
    }
    
    // Server Metrics Chart
    if (data.system_metrics.length > 0) {
        const metricsData = data.system_metrics.slice(0, 15).reverse();
        
        chartConfigs.server.data.labels = metricsData.map(d => new Date(d.timestamp).toLocaleTimeString());
        chartConfigs.server.data.datasets[0].data = metricsData.map(d => d.cpu_usage);
        chartConfigs.server.data.datasets[1].data = metricsData.map(d => d.memory_usage);
        chartConfigs.server.data.datasets[2].data = metricsData.map(d => d.disk_usage);
        chartConfigs.server.update('none');
    }
    
    // Weather Chart
    if (data.weather.length > 0) {
        const weatherByCity = {};
        data.weather.forEach(w => {
            if (!weatherByCity[w.city] || new Date(w.timestamp) > new Date(weatherByCity[w.city].timestamp)) {
                weatherByCity[w.city] = w;
            }
        });
        
        const cities = Object.keys(weatherByCity);
        const temps = cities.map(city => weatherByCity[city].temperature);
        
        chartConfigs.weather.data.labels = cities;
        chartConfigs.weather.data.datasets[0].data = temps;
        chartConfigs.weather.update('none');
    }
    
    // Social Media Chart
    if (data.social_media.length > 0) {
        const socialByPlatform = {};
        data.social_media.forEach(s => {
            if (!socialByPlatform[s.platform]) {
                socialByPlatform[s.platform] = [];
            }
            socialByPlatform[s.platform].push(s.engagement_rate);
        });
        
        const platforms = Object.keys(socialByPlatform);
        const avgEngagement = platforms.map(p => 
            socialByPlatform[p].reduce((a, b) => a + b, 0) / socialByPlatform[p].length
        );
        
        chartConfigs.social.data.labels = platforms;
        chartConfigs.social.data.datasets[0].data = avgEngagement;
        chartConfigs.social.update('none');
    }
    
    // Traffic Chart
    if (data.traffic.length > 0) {
        const trafficByLocation = {};
        data.traffic.forEach(t => {
            if (!trafficByLocation[t.location] || new Date(t.timestamp) > new Date(trafficByLocation[t.location].timestamp)) {
                trafficByLocation[t.location] = t;
            }
        });
        
        const locations = Object.keys(trafficByLocation);
        const vehicles = locations.map(loc => trafficByLocation[loc].vehicle_count);
        
        chartConfigs.traffic.data.labels = locations;
        chartConfigs.traffic.data.datasets[0].data = vehicles;
        chartConfigs.traffic.update('none');
    }
}

async function fetchAnalytics() {
    try {
        const response = await fetch('/api/analytics/');
        const analytics = await response.json();
        
        // Update Revenue Chart with aggregated data
        if (analytics.revenue_by_category && analytics.revenue_by_category.length > 0) {
            const categories = analytics.revenue_by_category.map(r => r.category);
            const revenues = analytics.revenue_by_category.map(r => r.total_revenue);
            
            chartConfigs.revenue.data.labels = categories;
            chartConfigs.revenue.data.datasets[0].data = revenues;
            chartConfigs.revenue.update('none');
        }
        
    } catch (error) {
        console.error('Error fetching analytics:', error);
    }
}

function updateTables(data) {
    // Sensor Table
    const sensorTbody = document.querySelector('#sensorTable tbody');
    sensorTbody.innerHTML = data.sensors.slice(0, 8).map(s => `
        <tr>
            <td>${s.sensor_id}</td>
            <td>${s.temperature.toFixed(1)}°C</td>
            <td>${s.humidity.toFixed(1)}%</td>
            <td><span class="badge ${s.status}">${s.status}</span></td>
        </tr>
    `).join('');
    
    // E-commerce Table
    const ecommerceTbody = document.querySelector('#ecommerceTable tbody');
    ecommerceTbody.innerHTML = data.ecommerce.slice(0, 8).map(t => `
        <tr>
            <td>${t.order_id}</td>
            <td>${t.product_name}</td>
            <td>$${t.amount.toFixed(2)}</td>
            <td>${t.customer_location}</td>
        </tr>
    `).join('');
    
    // Stock Table
    const stockTbody = document.querySelector('#stockTable tbody');
    const latestStocksBySymbol = {};
    data.stocks.forEach(s => {
        if (!latestStocksBySymbol[s.symbol] || new Date(s.timestamp) > new Date(latestStocksBySymbol[s.symbol].timestamp)) {
            latestStocksBySymbol[s.symbol] = s;
        }
    });
    
    stockTbody.innerHTML = Object.values(latestStocksBySymbol).slice(0, 6).map(s => `
        <tr>
            <td><strong>${s.symbol}</strong></td>
            <td>$${s.price.toFixed(2)}</td>
            <td class="${s.change_percent >= 0 ? 'positive' : 'negative'}">
                ${s.change_percent >= 0 ? '+' : ''}${s.change_percent.toFixed(2)}%
            </td>
            <td>${s.volume.toLocaleString()}</td>
        </tr>
    `).join('');
    
    // Traffic Table
    const trafficTbody = document.querySelector('#trafficTable tbody');
    trafficTbody.innerHTML = data.traffic.slice(0, 8).map(t => `
        <tr>
            <td>${t.location}</td>
            <td>${t.vehicle_count}</td>
            <td>${t.avg_speed.toFixed(1)} km/h</td>
            <td><span class="badge ${t.congestion_level.toLowerCase()}">${t.congestion_level}</span></td>
        </tr>
    `).join('');
}

// Initialize and start auto-update
initializeCharts();
fetchAllData();
setInterval(fetchAllData, 5000); // Update every 5 seconds

console.log('🚀 Advanced Dashboard initialized - MongoDB NoSQL Backend');
console.log('📊 Auto-updating every 5 seconds with 7 data sources');
