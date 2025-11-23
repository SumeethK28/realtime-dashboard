from datetime import datetime
from .db_utils import get_collection

class SensorData:
    """IoT Sensor data model using MongoDB"""
    
    @classmethod
    def create(cls, sensor_id, temperature, humidity, pressure, status='normal'):
        collection = get_collection('sensor_data')
        doc = {
            'sensor_id': sensor_id,
            'timestamp': datetime.now(),
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure,
            'status': status
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('sensor_data')
        return list(collection.find().sort('timestamp', -1).limit(limit))
    
    @classmethod
    def get_aggregated_stats(cls):
        """Get aggregated sensor statistics using MongoDB aggregation"""
        collection = get_collection('sensor_data')
        pipeline = [
            {
                '$group': {
                    '_id': '$sensor_id',
                    'avg_temp': {'$avg': '$temperature'},
                    'avg_humidity': {'$avg': '$humidity'},
                    'avg_pressure': {'$avg': '$pressure'},
                    'count': {'$sum': 1}
                }
            }
        ]
        return list(collection.aggregate(pipeline))

class SystemMetrics:
    """Server metrics model using MongoDB"""
    
    @classmethod
    def create(cls, cpu_usage, memory_usage, disk_usage, network_in, network_out):
        collection = get_collection('system_metrics')
        doc = {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage': disk_usage,
            'network_in': network_in,
            'network_out': network_out,
            'timestamp': datetime.now()
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('system_metrics')
        return list(collection.find().sort('timestamp', -1).limit(limit))

class StockData:
    """Stock market data model using MongoDB"""
    
    @classmethod
    def create(cls, symbol, price, volume, change_percent, market_cap=None):
        collection = get_collection('stock_data')
        doc = {
            'symbol': symbol,
            'price': price,
            'volume': volume,
            'change_percent': change_percent,
            'market_cap': market_cap,
            'timestamp': datetime.now()
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('stock_data')
        return list(collection.find().sort('timestamp', -1).limit(limit))

class WeatherData:
    """Weather data model using MongoDB"""
    
    @classmethod
    def create(cls, city, temperature, humidity, wind_speed, condition, pressure):
        collection = get_collection('weather_data')
        doc = {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'condition': condition,
            'pressure': pressure,
            'timestamp': datetime.now()
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('weather_data')
        return list(collection.find().sort('timestamp', -1).limit(limit))

class EcommerceTransaction:
    """E-commerce transaction model using MongoDB"""
    
    @classmethod
    def create(cls, order_id, product_name, category, amount, quantity, customer_location):
        collection = get_collection('ecommerce_transactions')
        doc = {
            'order_id': order_id,
            'product_name': product_name,
            'category': category,
            'amount': amount,
            'quantity': quantity,
            'customer_location': customer_location,
            'timestamp': datetime.now()
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('ecommerce_transactions')
        return list(collection.find().sort('timestamp', -1).limit(limit))
    
    @classmethod
    def get_revenue_by_category(cls):
        """Aggregate revenue by category using MongoDB"""
        collection = get_collection('ecommerce_transactions')
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
        return list(collection.aggregate(pipeline))

class SocialMediaMetrics:
    """Social media analytics model using MongoDB"""
    
    @classmethod
    def create(cls, platform, post_id, likes, shares, comments, engagement_rate):
        collection = get_collection('social_media_metrics')
        doc = {
            'platform': platform,
            'post_id': post_id,
            'likes': likes,
            'shares': shares,
            'comments': comments,
            'engagement_rate': engagement_rate,
            'timestamp': datetime.now()
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('social_media_metrics')
        return list(collection.find().sort('timestamp', -1).limit(limit))

class TrafficData:
    """Traffic monitoring data model using MongoDB"""
    
    @classmethod
    def create(cls, location, vehicle_count, avg_speed, congestion_level):
        collection = get_collection('traffic_data')
        doc = {
            'location': location,
            'vehicle_count': vehicle_count,
            'avg_speed': avg_speed,
            'congestion_level': congestion_level,
            'timestamp': datetime.now()
        }
        result = collection.insert_one(doc)
        doc['_id'] = result.inserted_id
        return doc
    
    @classmethod
    def get_latest(cls, limit=50):
        collection = get_collection('traffic_data')
        return list(collection.find().sort('timestamp', -1).limit(limit))
