import time
import random
import string
from datetime import datetime
from .models_advanced import (
    SensorData, SystemMetrics, StockData, WeatherData,
    EcommerceTransaction, SocialMediaMetrics, TrafficData
)

def generate_order_id():
    """Generate random order ID"""
    return 'ORD' + ''.join(random.choices(string.digits, k=8))

def generate_post_id():
    """Generate random post ID"""
    return 'POST' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def run_advanced_data_simulation():
    """Generate simulated data for all data sources"""
    
    # Configuration
    sensor_ids = ['SENSOR_001', 'SENSOR_002', 'SENSOR_003', 'SENSOR_004']
    
    stocks = {
        'AAPL': 150.00,
        'GOOGL': 2800.00,
        'MSFT': 300.00,
        'TSLA': 700.00,
        'AMZN': 3200.00,
        'META': 280.00
    }
    
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy', 'Stormy']
    
    product_categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports', 'Toys']
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smart Watch'],
        'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Hat'],
        'Books': ['Fiction Novel', 'Programming Book', 'Biography', 'Cook Book', 'Self-Help'],
        'Home & Kitchen': ['Blender', 'Coffee Maker', 'Vacuum Cleaner', 'Microwave', 'Toaster'],
        'Sports': ['Basketball', 'Tennis Racket', 'Yoga Mat', 'Dumbbells', 'Running Shoes'],
        'Toys': ['Action Figure', 'Board Game', 'Puzzle', 'RC Car', 'Doll']
    }
    
    customer_locations = ['California', 'Texas', 'New York', 'Florida', 'Illinois', 'Washington']
    
    social_platforms = ['Twitter', 'Facebook', 'Instagram', 'LinkedIn', 'TikTok']
    
    traffic_locations = [
        'Highway 101 North',
        'Downtown Main St',
        'Airport Freeway',
        'Broadway Ave',
        'Fifth Avenue'
    ]
    
    print("=" * 80)
    print("🚀 Starting ADVANCED Real-Time Data Simulation with 7 Data Sources")
    print("=" * 80)
    print("📊 Data Sources:")
    print("   1. IoT Sensors (Temperature, Humidity, Pressure)")
    print("   2. Server Metrics (CPU, Memory, Disk, Network)")
    print("   3. Stock Market (6 stocks)")
    print("   4. Weather Data (5 cities)")
    print("   5. E-commerce Transactions (6 categories)")
    print("   6. Social Media Analytics (5 platforms)")
    print("   7. Traffic Monitoring (5 locations)")
    print("=" * 80)
    
    iteration = 0
    
    while True:
        iteration += 1
        print(f"\n📡 Iteration {iteration} - {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 80)
        
        # 1. Generate IoT Sensor Data
        print("📡 1. Generating IoT Sensor Data...")
        for sensor_id in sensor_ids:
            temperature = round(random.uniform(18.0, 32.0), 2)
            humidity = round(random.uniform(30.0, 90.0), 2)
            pressure = round(random.uniform(980.0, 1025.0), 2)
            status = 'normal' if temperature < 30 else 'warning'
            
            SensorData.create(
                sensor_id=sensor_id,
                temperature=temperature,
                humidity=humidity,
                pressure=pressure,
                status=status
            )
            print(f"   ✅ {sensor_id}: {temperature}°C, {humidity}%, {pressure}hPa [{status}]")
        
        # 2. Generate Server Metrics
        print("\n💻 2. Generating Server Metrics...")
        cpu = round(random.uniform(15.0, 85.0), 2)
        memory = round(random.uniform(40.0, 90.0), 2)
        disk = round(random.uniform(50.0, 85.0), 2)
        net_in = round(random.uniform(1.0, 100.0), 2)
        net_out = round(random.uniform(1.0, 100.0), 2)
        
        SystemMetrics.create(
            cpu_usage=cpu,
            memory_usage=memory,
            disk_usage=disk,
            network_in=net_in,
            network_out=net_out
        )
        print(f"   ✅ CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
        print(f"   ✅ Network: ↓{net_in} MB/s | ↑{net_out} MB/s")
        
        # 3. Generate Stock Market Data
        print("\n📈 3. Generating Stock Market Data...")
        for symbol, base_price in stocks.items():
            change = random.uniform(-10, 10)
            new_price = round(base_price + change, 2)
            stocks[symbol] = new_price
            
            volume = random.randint(500000, 2000000)
            change_percent = round((change / base_price) * 100, 2)
            market_cap = round(new_price * random.randint(100, 500), 2)
            
            StockData.create(
                symbol=symbol,
                price=new_price,
                volume=volume,
                change_percent=change_percent,
                market_cap=market_cap
            )
            
            arrow = "↑" if change_percent >= 0 else "↓"
            color = "+" if change_percent >= 0 else ""
            print(f"   ✅ {symbol}: ${new_price} {arrow} {color}{change_percent}%")
        
        # 4. Generate Weather Data
        print("\n🌤️  4. Generating Weather Data...")
        for city in cities:
            temp = round(random.uniform(10.0, 35.0), 1)
            humidity = round(random.uniform(40.0, 95.0), 1)
            wind = round(random.uniform(5.0, 30.0), 1)
            condition = random.choice(weather_conditions)
            pressure = round(random.uniform(1000.0, 1020.0), 1)
            
            WeatherData.create(
                city=city,
                temperature=temp,
                humidity=humidity,
                wind_speed=wind,
                condition=condition,
                pressure=pressure
            )
            print(f"   ✅ {city}: {temp}°C, {condition}, Wind: {wind} km/h")
        
        # 5. Generate E-commerce Transactions (2-4 per iteration)
        print("\n🛒 5. Generating E-commerce Transactions...")
        num_transactions = random.randint(2, 4)
        for _ in range(num_transactions):
            category = random.choice(product_categories)
            product = random.choice(products[category])
            amount = round(random.uniform(10.0, 500.0), 2)
            quantity = random.randint(1, 5)
            location = random.choice(customer_locations)
            order_id = generate_order_id()
            
            EcommerceTransaction.create(
                order_id=order_id,
                product_name=product,
                category=category,
                amount=amount,
                quantity=quantity,
                customer_location=location
            )
            print(f"   ✅ {order_id}: {product} ({category}) - ${amount} x {quantity} [{location}]")
        
        # 6. Generate Social Media Metrics
        print("\n📱 6. Generating Social Media Metrics...")
        for platform in social_platforms:
            likes = random.randint(100, 10000)
            shares = random.randint(10, 2000)
            comments = random.randint(5, 500)
            total_engagement = likes + shares + comments
            engagement_rate = round((total_engagement / 10000) * 100, 2)
            post_id = generate_post_id()
            
            SocialMediaMetrics.create(
                platform=platform,
                post_id=post_id,
                likes=likes,
                shares=shares,
                comments=comments,
                engagement_rate=engagement_rate
            )
            print(f"   ✅ {platform} ({post_id}): {likes} ❤️ | {shares} 🔄 | {comments} 💬")
        
        # 7. Generate Traffic Data
        print("\n🚗 7. Generating Traffic Data...")
        for location in traffic_locations:
            vehicle_count = random.randint(50, 500)
            avg_speed = round(random.uniform(20.0, 100.0), 1)
            
            if avg_speed < 30:
                congestion = 'High'
            elif avg_speed < 60:
                congestion = 'Medium'
            else:
                congestion = 'Low'
            
            TrafficData.create(
                location=location,
                vehicle_count=vehicle_count,
                avg_speed=avg_speed,
                congestion_level=congestion
            )
            print(f"   ✅ {location}: {vehicle_count} vehicles, {avg_speed} km/h [{congestion}]")
        
        print("-" * 80)
        print(f"⏱️  Waiting 5 seconds before next iteration...\n")
        time.sleep(5)
