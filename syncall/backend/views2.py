import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

#create your views here
class WeatherHistory(View):
    def get(self, request):
        lt = request.GET.get('lattitude')
        ln = request.GET.get('longitude')

        api_call = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiweather.weatherii.weatherhistory.main?lon=139&lat=35'
        headers = {
                    'Content-Type' : 'application/json',    
                    'Authorization' : 'Bearer {token}',
        }

        response = requests.get(api_call, headers=headers)

        #condition to check the API call is successful or not
        if response.status_code == 200:
            json_result = response.json()
            History_list = json_result['response']['jsonDoc']['result']

            #Extract the required data from the API response
            extracted_data = []
            for history_entry in History_list:
                mean_temp = history_entry['temp']['mean']
                mean_pressure = history_entry['pressure']['mean']
                mean_humidity = history_entry['humidity']['mean']
                mean_clouds = history_entry['clouds']['mean']
                mean_precipitation = history_entry['precipitation']['mean']
                extracted_data.append({
                    'mean_temp': mean_temp,
                    'mean_pressure': mean_pressure,
                    'mean_humidity': mean_humidity,
                    'mean_clouds': mean_clouds,
                    'mean_precipitation': mean_precipitation,
                })
            return JsonResponse({'weather_history' : extracted_data})
        
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)
