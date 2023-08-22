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
                    'Authorization' : 'Bearer 6KPnAjasx2BzGyQSF2Lnfw51zqpeNjBy5lHN66E8Fgw5s8dxWsDmpr5DQQAOP7uBKhwOeYrBljpGnJKrpaUWEQ6h9JmFScSEHjiYZQ1NZXVIr+OTK6TXB2NWImPfVdzpwg033S0QyQ5jPJFnwwViuGFxW+QXqxoyJWY3h0Kago8G85t4pN6b3Vt88TjwMuK/BqG0RO2rP2H9mGa1GwrrEGbu0NbS5TPRj1XmVzmBHkJGVdkZKdFcF1u/b2h9TjytIJlyyCvbcFsSZNy8biSWe/dEXmQAH+37q3SuNecjjTVjnE+NexbNjPmpxkFurpBqcTJARvA0SJxE/4lzBNfKyfEOey0InePOX6UzcrQHWP7hYX83HbTQRNh0h5D0rfSu1FQaaSXpP3HMBlQKuKHwnQbwPmoDK1hdR+B92YPk+YC6kpDHnv5Eg/PY8ZMVwcr2c1ogeao+2XobkxUT5qQimo+7As8AD7Eb2lpCe375WXDCgFB6kzMViR7kYArHbfOXINPTWy+dOOLKzc37ode0gQ==',
        }

        response = requests.get(api_call, headers=headers)

        #condition to check the API call is successful or not
        if response.status_code == 200:
            json_result = response.json()
            return JsonResponse(json_result)
        
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)