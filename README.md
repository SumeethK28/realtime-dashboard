# 🚀 Real-Time Dashboard using MongoDB (NoSQL)

## 📋 Project Overview
This is an **Advanced Real-Time Dashboard** built with **Django** and **MongoDB (NoSQL)** that visualizes data from **7 different real-time data sources** with live updates every 5 seconds.

### ✨ Key Features
- ✅ **MongoDB NoSQL Database** - Document-based storage for flexible schema
- ✅ **Real-Time Data Updates** - Auto-refresh every 5 seconds
- ✅ **7 Data Sources** - Diverse real-world data simulation
- ✅ **Multiple Chart Types** - Line, Bar, Radar, Dual-Axis charts
- ✅ **MongoDB Aggregations** - Advanced analytics using aggregation pipeline
- ✅ **Responsive Design** - Modern, professional UI
- ✅ **Live Statistics** - Real-time KPIs and metrics

---

## 📊 Data Sources

### 1. **IoT Sensor Data** 📡
- Temperature, Humidity, Pressure monitoring
- 4 sensors with normal/warning status
- MongoDB collection: `sensor_data`

### 2. **Server Metrics** 💻
- CPU, Memory, Disk Usage
- Network I/O (incoming/outgoing)
- MongoDB collection: `system_metrics`

### 3. **Stock Market Data** 📈
- 6 stocks: AAPL, GOOGL, MSFT, TSLA, AMZN, META
- Price, Volume, Change %, Market Cap
- MongoDB collection: `stock_data`

### 4. **Weather Data** 🌤️
- 5 cities: New York, Los Angeles, Chicago, Houston, Phoenix
- Temperature, Humidity, Wind Speed, Conditions
- MongoDB collection: `weather_data`

### 5. **E-commerce Transactions** 🛒
- 6 product categories
- Order tracking, Revenue analytics
- MongoDB collection: `ecommerce_transactions`
- **MongoDB Aggregation**: Revenue by category

### 6. **Social Media Analytics** 📱
- 5 platforms: Twitter, Facebook, Instagram, LinkedIn, TikTok
- Likes, Shares, Comments, Engagement Rate
- MongoDB collection: `social_media_metrics`

### 7. **Traffic Monitoring** 🚗
- 5 locations with vehicle counts
- Average speed, Congestion levels
- MongoDB collection: `traffic_data`

---

## 🗄️ MongoDB NoSQL Implementation

### Why MongoDB (NoSQL)?
- **Flexible Schema**: Each data source has different fields
- **High Performance**: Fast writes for real-time data
- **Scalability**: Handles large volumes of time-series data
- **Aggregation Framework**: Powerful analytics (revenue by category, sensor stats)
- **Document Model**: Natural fit for JSON-like data

### MongoDB Collections
```javascript
// sensor_data
{
  _id: ObjectId,
  sensor_id: String,
  timestamp: DateTime,
  temperature: Number,
  humidity: Number,
  pressure: Number,
  status: String
}

// ecommerce_transactions
{
  _id: ObjectId,
  order_id: String,
  product_name: String,
  category: String,
  amount: Number,
  quantity: Number,
  customer_location: String,
  timestamp: DateTime
}

// ... 5 more collections
```

### MongoDB Aggregations Used
```python
# Revenue by Category (Aggregation Pipeline)
pipeline = [
    {
        '$group': {
            '_id': '$category',
            'total_revenue': {'$sum': '$amount'},
            'total_orders': {'$sum': 1}
        }
    },
    {'$sort': {'total_revenue': -1}}
]

# Sensor Statistics (Aggregation Pipeline)
pipeline = [
    {
        '$group': {
            '_id': '$sensor_id',
            'avg_temp': {'$avg': '$temperature'},
            'avg_humidity': {'$avg': '$humidity'},
            'count': {'$sum': 1}
        }
    }
]
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Django 5.2.8 |
| **NoSQL Database** | MongoDB 5.0+ |
| **Python MongoDB Driver** | PyMongo 3.11.4 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Charts** | Chart.js 3.x |
| **Real-time Updates** | AJAX Polling (5s interval) |
| **Python Version** | Python 3.12 |

---

## 📁 Project Structure

```
realtime-dashboard/
├── dashboard_app/                  # Main Django app
│   ├── models_advanced.py          # 7 MongoDB model classes
│   ├── views_advanced.py           # API endpoints + aggregations
│   ├── data_generator_advanced.py  # Real-time data simulator
│   ├── db_utils.py                 # MongoDB connection utility
│   ├── urls.py                     # URL routing
│   ├── templates/
│   │   └── dashboard/
│   │       └── advanced_dashboard.html  # Main dashboard UI
│   └── management/
│       └── commands/
│           └── generate_data.py    # Django management command
├── dashboard_project/              # Django project settings
│   ├── settings.py                 # Production-ready settings
│   ├── urls.py                     # Root URL configuration
│   ├── wsgi.py                     # WSGI entry point
│   └── asgi.py                     # ASGI entry point
├── static/
│   ├── js/
│   │   └── advanced_dashboard.js   # Chart.js visualization logic
│   ├── css/                        # Stylesheets
│   └── images/                     # Static images
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
├── build.sh                        # Render build script
├── Procfile                        # Process file for deployment
├── render.yaml                     # Render configuration
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── DEPLOYMENT.md                   # Deployment guide
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12
- MongoDB 5.0+ (running on localhost:27017)
- Virtual environment (recommended)

### Step 1: Install Dependencies
```bash
cd realtime-dashboard
source bda/bin/activate
pip install -r requirements.txt
```

### Step 2: Start MongoDB
```bash
# Linux/Mac
sudo systemctl start mongod

# Or Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

### Step 3: Run Django Server
```bash
python manage.py runserver
```

### Step 4: Start Data Generator (New Terminal)
```bash
source bda/bin/activate
python manage.py generate_data
```

### Step 5: Access Dashboard
```
Advanced Dashboard: http://127.0.0.1:8000/
```

---

## 📊 Dashboard Features

### Real-Time Statistics (Top Cards)
- 📡 Average Temperature from IoT sensors
- 💻 Current CPU Usage
- 📈 Average Stock Price across 6 stocks
- 🛒 Total Revenue from transactions
- ❤️ Social Media Total Engagement
- 🚗 Average Traffic Vehicle Count

### Interactive Charts
1. **Temperature vs Stock Prices** (Dual-Axis Line Chart)
2. **Server Performance Metrics** (Multi-Line Chart)
3. **Revenue by Category** (Bar Chart with MongoDB Aggregation)
4. **Social Media Engagement** (Radar Chart)
5. **Weather Across Cities** (Bar Chart)
6. **Traffic Congestion** (Horizontal Bar Chart)

### Data Tables
- Recent IoT Sensor Readings
- Latest E-commerce Transactions
- Stock Market Updates
- Traffic Monitoring Status

---

## 🔥 MongoDB NoSQL Advantages Demonstrated

### 1. **Flexible Schema**
- Different data sources with different fields
- No need for complex SQL joins
- Easy to add new fields without migrations

### 2. **Fast Writes**
- Handles 50+ inserts per second
- Optimized for time-series data
- No table locks or complex transactions

### 3. **Aggregation Framework**
```python
# Complex analytics in a single query
EcommerceTransaction.get_revenue_by_category()
# Returns revenue grouped by category, sorted by total
```

### 4. **Scalability**
- Horizontal scaling ready
- Sharding support for large datasets
- Replica sets for high availability

### 5. **JSON-Native**
- Data stored as BSON (Binary JSON)
- Easy API integration
- Natural fit for web applications

---

## 📈 Sample Data Generation

The data generator creates realistic data:

```python
# IoT Sensors: Every 5 seconds
- 4 sensors × 3 readings = 12 data points
- Temperature: 18-32°C
- Humidity: 30-90%
- Pressure: 980-1025 hPa

# Stock Market: Every 5 seconds
- 6 stocks with random price fluctuations
- ±10% change simulation
- Realistic volume: 500K-2M

# E-commerce: 2-4 transactions every 5 seconds
- 6 categories × 5 products each
- Prices: $10-$500
- 6 customer locations

# Weather: Every 5 seconds for 5 cities
# Social Media: Every 5 seconds for 5 platforms
# Traffic: Every 5 seconds for 5 locations
```

**Total**: ~70+ documents inserted into MongoDB every 5 seconds!

---

## 🎯 Project Objectives Met

✅ **Real-time data visualization**  
✅ **NoSQL database (MongoDB) implementation**  
✅ **Multiple diverse data sources (7 types)**  
✅ **Advanced analytics using MongoDB aggregations**  
✅ **Multiple chart types and visualizations**  
✅ **Professional, responsive UI**  
✅ **Auto-refresh without page reload**  
✅ **Scalable architecture**  

---

## 🔄 Auto-Update Mechanism

```javascript
// Frontend polls API every 5 seconds
setInterval(fetchAllData, 5000);

// Backend continuously generates new data
while True:
    generate_all_data_sources()
    time.sleep(5)  # Wait 5 seconds
```

---

## 📸 Screenshots

### Advanced Dashboard
- 6 real-time statistics cards
- 6 interactive charts (Line, Bar, Radar)
- 4 data tables with live updates
- Gradient background with modern design

---

## 🚀 Future Enhancements

- [ ] WebSocket implementation for instant updates (currently using AJAX polling)
- [ ] User authentication and personalized dashboards
- [ ] Data export (CSV, PDF, Excel)
- [ ] Historical data analysis and trends
- [ ] Alert system for threshold violations (email/SMS)
- [ ] Machine learning predictions
- [ ] Mobile app version (React Native)
- [ ] MongoDB Atlas cloud deployment
- [ ] Data retention policies (auto-delete old data)
- [ ] Multi-language support

---

## 🐛 Troubleshooting

### Dashboard shows "--" values
- **Solution**: Hard refresh browser (Ctrl+Shift+R or Ctrl+F5) to clear JavaScript cache
- The JavaScript file has cache-busting version parameter (`?v=2`)

### MongoDB connection errors
```bash
# Check if MongoDB is running
sudo systemctl status mongod

# Or check with mongo shell
mongosh
```

### Data not generating
- Ensure data generator is running in separate terminal
- Check terminal for error messages
- Verify MongoDB connection in terminal output

---

## 📝 API Endpoints

```
GET /                       # Advanced Dashboard (Default)
GET /api/all-data/          # All data sources (combined JSON)
GET /api/analytics/         # MongoDB aggregation analytics
```

**Note**: Single-purpose API endpoints for individual data sources have been consolidated into `/api/all-data/` for efficiency.

---

## 👨‍💻 Developer Notes

### MongoDB Connection
```python
# db_utils.py - Lazy loading to avoid Django settings issues
from pymongo import MongoClient
from django.conf import settings

_client = None
_db = None

def get_db():
    global _client, _db
    if _db is None:
        _client = MongoClient(settings.MONGODB_SETTINGS['host'])
        _db = _client[settings.MONGODB_SETTINGS['db_name']]
    return _db
```

### Adding New Data Source
1. Create model class in `models_advanced.py`
2. Add generation logic in `data_generator_advanced.py`
3. Create API endpoint in `views_advanced.py`
4. Update frontend in `advanced_dashboard.js`

### Cache-Busting
- JavaScript file uses version parameter: `/static/js/advanced_dashboard.js?v=2`
- Increment version number when updating JavaScript to force browser reload

---

## 📚 Learning Outcomes

This project demonstrates:
- MongoDB NoSQL database operations
- Real-time data streaming
- Chart.js visualization library
- Django REST APIs
- Asynchronous JavaScript (AJAX)
- MongoDB Aggregation Framework
- Time-series data handling
- Responsive web design

---

## 🤝 Contributing

This is a college project demonstrating NoSQL database concepts with real-time data visualization.

---

## 📄 License

Educational project - Free to use for learning purposes

---

## 📞 Contact

For questions about this project, please refer to the project documentation or MongoDB official docs.

---

**Built with ❤️ using MongoDB, Django, and Chart.js**
