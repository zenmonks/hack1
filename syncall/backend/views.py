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
                    'Authorization' : 'Bearer {6KPnAjasx2BzGyQSF2Lnfw51zqpeNjBy5lHN66E8Fgw5s8dxWsDmpr5DQQAOP7uBKhwOeYrBljpGnJKrpaUWEQ6h9JmFScSEHjiYZQ1NZXVIr+OTK6TXB2NWImPfVdzpwg033S0QyQ5jPJFnwwViuGFxW+QXqxoyJWY3h0Kago8G85t4pN6b3Vt88TjwMuK/BqG0RO2rP2H9mGa1GwrrEGbu0NbS5TPRj1XmVzmBHkJGVdkZKdFcF1u/b2h9TjytIJlyyCvbcFsSZNy8biSWe/dEXmQAH+37q3SuNecjjTV1pV070TZiuGGGtrzRC3ywhtCJHJAxHXUalC6CAEP9ePEOey0InePOX6UzcrQHWP7hYX83HbTQRNh0h5D0rfSu1FQaaSXpP3HMBlQKuKHwnQbwPmoDK1hdR+B92YPk+YC6kpDHnv5Eg/PY8ZMVwcr2LLhxu0CuZM9iewU7OB5M6NS3Xe4yGguX1giyyrfqy+FOlu4a8rO5reZ0KQo9ObPrINPTWy+dOOLKzc37ode0gQ==}'
                 }
        response = requests.get(api_url, headers=headers)

        #check the API call is successful or not
        if response.status_code == 200:
            json_data = response.json()
            return JsonResponse(json_data)
            
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)
            