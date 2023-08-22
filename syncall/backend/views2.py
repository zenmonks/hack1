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
            return JsonResponse(json_result)
        
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)
