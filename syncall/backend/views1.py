import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


# Create your views here.
class WeatherForecast(View):
    def get(self, request):
        #Get the location coordinates from the frontend
        lat = request.GET.get('lattitude')
        lon = request.GET.get('longitude')

        #Get the weather forecast from the API
        api_url = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiapp.weather.weatherforecast.main?lat=23.831457&lon=91.286778'
        headers = { 
                    'Content-Type' : 'application/json',
                    'Authorization' : 'Bearer {token}'
                 }   #11:20
        response = requests.get(api_url, headers=headers)

        #check the API call is successful or not
        if response.status_code == 200:

            json_data = response.json()
            Forecast_list = json_data['response']['jsonDoc']['list']
            
            #Extract the required data from the API response
            extracted_data = []
            for forecast_entry in Forecast_list:
                dt = forecast_entry['dt_txt']
                temp = forecast_entry['main']['temp']
                feels_like = forecast_entry['main']['feels_like']
                weather_list = forecast_entry['weather'][0]
                description = weather_list['description']
                main = weather_list['main']
                humidity = forecast_entry['main']['humidity']
                extracted_data.append({
                'dt': dt,
                'temp': temp,
                'humidity': humidity,
                'description': description,
                'feels_like': feels_like,
                'main': main,
            })
        

            return JsonResponse({'weather_data': extracted_data})  
          
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)
            