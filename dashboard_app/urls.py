from django.urls import path
from . import views_advanced

urlpatterns = [
    # Advanced dashboard as default
    path('', views_advanced.advanced_dashboard, name='dashboard'),
    path('api/all-data/', views_advanced.api_all_data, name='api_all_data'),
    path('api/analytics/', views_advanced.api_analytics, name='api_analytics'),
]