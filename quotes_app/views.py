from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


from django.shortcuts import render

class WeatherAPIView(APIView):
    http_method_names = ["get"]  # Explicitly allow GET requests
    permission_classes = [AllowAny]  # Allow public access



def weather_view1(request):
    if request.method == "GET":
        city = request.GET.get("city", "Unknown")
        return JsonResponse({"message": f"Weather data for {city}"})
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

@api_view(['GET'])
def weather_page(request):
    return render(request, 'quotes_app/weather.html')

def weather_view(request):
    city = request.GET.get("city", "Dublin")  # Default city if not provided
    api_key = "ed2c16c91176d2d1879f39e344afa12e"  # Replace with your OpenWeather API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return Response(data)  # Return OpenWeather API response
    else:
        return Response({"error": "Failed to fetch weather data"}, status=response.status_code)




def home(request):
    return render(request, 'quotes_app/index.html')  # Loads index.html from templates folder


class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
