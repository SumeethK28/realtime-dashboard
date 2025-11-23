from pymongo import MongoClient

_client = None
_db = None

def get_db():
    """Lazy-load MongoDB connection"""
    global _client, _db
    if _db is None:
        from django.conf import settings
        _client = MongoClient(settings.MONGODB_SETTINGS['host'])
        _db = _client[settings.MONGODB_SETTINGS['db_name']]
    return _db

def get_collection(name):
    """Get a MongoDB collection"""
    db = get_db()
    return db[name]

# Collection getters
def get_sensor_data_collection():
    return get_collection('sensor_data')

def get_system_metrics_collection():
    return get_collection('system_metrics')