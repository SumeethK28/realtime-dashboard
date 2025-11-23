from django.shortcuts import render
from django.http import JsonResponse
from .models_advanced import (
    SensorData, SystemMetrics, StockData, WeatherData,
    EcommerceTransaction, SocialMediaMetrics, TrafficData
)

def advanced_dashboard(request):
    """Main advanced dashboard view"""
    return render(request, 'dashboard/advanced_dashboard.html')

def api_all_data(request):
    """Combined API endpoint for all data sources"""
    try:
        response_data = {
            'sensors': [],
            'system_metrics': [],
            'stocks': [],
            'weather': [],
            'ecommerce': [],
            'social_media': [],
            'traffic': []
        }
        
        # Get sensor data
        sensors = SensorData.get_latest(20)
        response_data['sensors'] = [
            {
                'sensor_id': item['sensor_id'],
                'temperature': item['temperature'],
                'humidity': item['humidity'],
                'pressure': item['pressure'],
                'status': item['status'],
                'timestamp': item['timestamp'].isoformat()
            }
            for item in sensors
        ]
        
        # Get system metrics
        metrics = SystemMetrics.get_latest(20)
        response_data['system_metrics'] = [
            {
                'cpu_usage': item['cpu_usage'],
                'memory_usage': item['memory_usage'],
                'disk_usage': item['disk_usage'],
                'network_in': item['network_in'],
                'network_out': item['network_out'],
                'timestamp': item['timestamp'].isoformat()
            }
            for item in metrics
        ]
        
        # Get stock data
        stocks = StockData.get_latest(30)
        response_data['stocks'] = [
            {
                'symbol': item['symbol'],
                'price': item['price'],
                'volume': item['volume'],
                'change_percent': item['change_percent'],
                'market_cap': item.get('market_cap'),
                'timestamp': item['timestamp'].isoformat()
            }
            for item in stocks
        ]
        
        # Get weather data
        weather = WeatherData.get_latest(25)
        response_data['weather'] = [
            {
                'city': item['city'],
                'temperature': item['temperature'],
                'humidity': item['humidity'],
                'wind_speed': item['wind_speed'],
                'condition': item['condition'],
                'pressure': item['pressure'],
                'timestamp': item['timestamp'].isoformat()
            }
            for item in weather
        ]
        
        # Get ecommerce transactions
        transactions = EcommerceTransaction.get_latest(20)
        response_data['ecommerce'] = [
            {
                'order_id': item['order_id'],
                'product_name': item['product_name'],
                'category': item['category'],
                'amount': item['amount'],
                'quantity': item['quantity'],
                'customer_location': item['customer_location'],
                'timestamp': item['timestamp'].isoformat()
            }
            for item in transactions
        ]
        
        # Get social media metrics
        social = SocialMediaMetrics.get_latest(25)
        response_data['social_media'] = [
            {
                'platform': item['platform'],
                'post_id': item['post_id'],
                'likes': item['likes'],
                'shares': item['shares'],
                'comments': item['comments'],
                'engagement_rate': item['engagement_rate'],
                'timestamp': item['timestamp'].isoformat()
            }
            for item in social
        ]
        
        # Get traffic data
        traffic = TrafficData.get_latest(25)
        response_data['traffic'] = [
            {
                'location': item['location'],
                'vehicle_count': item['vehicle_count'],
                'avg_speed': item['avg_speed'],
                'congestion_level': item['congestion_level'],
                'timestamp': item['timestamp'].isoformat()
            }
            for item in traffic
        ]
        
        return JsonResponse(response_data, safe=False)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def api_analytics(request):
    """MongoDB aggregation analytics"""
    try:
        analytics = {
            'sensor_stats': SensorData.get_aggregated_stats(),
            'revenue_by_category': EcommerceTransaction.get_revenue_by_category()
        }
        
        # Format sensor stats
        analytics['sensor_stats'] = [
            {
                'sensor_id': item['_id'],
                'avg_temp': round(item['avg_temp'], 2),
                'avg_humidity': round(item['avg_humidity'], 2),
                'avg_pressure': round(item['avg_pressure'], 2),
                'count': item['count']
            }
            for item in analytics['sensor_stats']
        ]
        
        # Format revenue stats
        analytics['revenue_by_category'] = [
            {
                'category': item['_id'],
                'total_revenue': round(item['total_revenue'], 2),
                'total_orders': item['total_orders']
            }
            for item in analytics['revenue_by_category']
        ]
        
        return JsonResponse(analytics)
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
