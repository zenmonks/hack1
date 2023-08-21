import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


# Create your views here.
class WeatherForecast(View):
    def get(self, request):
        #Getthe location coordinates from the frontend
        lat = request.GET.get('lattitude')
        lon = request.GET.get('longitude')

        #Get the weather forecast from the API
        api_url = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiapp.weather.weatherforecast.main?lat=23.831457&lon=91.286778'
        headers = { 
                    'Content-Type' : 'application/json',
                    'Authorization' : 'Bearer {token}'
                 }
        response = requests.get(api_url, headers=headers)

        #check the API call is successful or not
        if response.status_code == 200:
            json_data = response.json()
            return JsonResponse(json_data)
            
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)
            