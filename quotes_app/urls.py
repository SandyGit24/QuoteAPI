
from .views import home, QuoteListCreateView, QuoteDetailView, weather_page, weather_view

from django.urls import path
from .views import WeatherAPIView

urlpatterns = [

    path('', home, name='home'),  # This makes http://127.0.0.1:8000/ work
    path('quotes/', QuoteListCreateView.as_view(), name='quote-list'),
    path('quotes/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),

    path('weather/', WeatherAPIView.as_view(), name='weather-api'),  # API Endpoint
    path('weather-page/', weather_page, name='weather-page'),  # Frontend Page
    path('weather/', weather_view, name='weather')
]
