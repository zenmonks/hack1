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
                    'Authorization' : 'Bearer 6KPnAjasx2BzGyQSF2Lnfw51zqpeNjBy5lHN66E8Fgw5s8dxWsDmpr5DQQAOP7uBKhwOeYrBljpGnJKrpaUWEQ6h9JmFScSEHjiYZQ1NZXVIr+OTK6TXB2NWImPfVdzpwg033S0QyQ5jPJFnwwViuGFxW+QXqxoyJWY3h0Kago8G85t4pN6b3Vt88TjwMuK/BqG0RO2rP2H9mGa1GwrrEGbu0NbS5TPRj1XmVzmBHkJGVdkZKdFcF1u/b2h9TjytIJlyyCvbcFsSZNy8biSWe/dEXmQAH+37q3SuNecjjTV1RqUZzab7OGsylWRiX2O/ef9sYYp1SUOIkD5du7y7NvEOey0InePOX6UzcrQHWP7hYX83HbTQRNh0h5D0rfSu1FQaaSXpP3HMBlQKuKHwnQbwPmoDK1hdR+B92YPk+YC6kpDHnv5Eg/PY8ZMVwcr2hJH4jFpnP8kZOpIMNAiqepx+1mQfSfTKTKiO1iSVrxdj/+cZ/XUVTofFPQ4kSQdYINPTWy+dOOLKzc37ode0gQ==',
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

                mean_values = self.history_mean(extracted_data)

            return JsonResponse({'mean_values' : mean_values})
        
        else:
            error_message = {'error' : 'Something went wrong'}
            return JsonResponse(error_message)
        
    def history_mean(self, extracted_data):
        num_entries = len(extracted_data)
        sum_values = {
            'sum_temp': 0,
            'sum_humidity': 0,
            'sum_clouds': 0,
            'sum_precipitation':0,
        }

        for entry in extracted_data:
            sum_values['sum_temp'] += entry['mean_temp']
            sum_values['sum_humidity'] += entry['mean_humidity']
            sum_values['sum_precipitation'] += entry['mean_precipitation']
            sum_values['sum_clouds'] += entry['mean_clouds']

        mean_values = {
            'temp' : sum_values['sum_temp']/num_entries,
            'humidity' : sum_values['sum_humidity']/num_entries,
            'clouds' : sum_values['sum_clouds']/num_entries,
            'precipitation' : sum_values['sum_precipitation']/num_entries,
        }
     
        return mean_values

        