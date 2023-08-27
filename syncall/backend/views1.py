import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .algorithm import activity_planner


# Create your views here.
class WeatherForecast(View):
    def html_view(request):
        return render(request, 'index.html')
    def get(self, request):
        #Get the location coordinates from the frontend
        if request.method == 'GET':
           zipCode = request.GET.get('zipCode')
           countryCode = request.GET.get('countryCode')
           print(zipCode)
           print(countryCode)
           geocoding_api_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipCode},{countryCode}&appid=8e9c8389bf66ef430ffa5a19af301e17'
        
        geocoding_response = requests.get(geocoding_api_url)
        geocoding_data = geocoding_response.json()
        
        lat = geocoding_data['lat']
        lon = geocoding_data['lon']
        
        #Get the weather forecast from the API
        api_url = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiapp.weather.weatherforecast.main?lat={lat}&lon={lon}'
        api_call = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiweather.weatherii.weatherhistory.main?lat={lat}&lon={lon}'
        headers = { 
                    'Content-Type' : 'application/json',
                    'Authorization' : 'Bearer 6KPnAjasx2BzGyQSF2Lnfw51zqpeNjBy5lHN66E8Fgw5s8dxWsDmpr5DQQAOP7uBKhwOeYrBljpGnJKrpaUWEQ6h9JmFScSEHjiYZQ1NZXVIr+OTK6TXB2NWImPfVdzpwg033S0QyQ5jPJFnwwViuGFxW+QXqxoyJWY3h0Kago8G85t4pN6b3Vt88TjwMuK/BqG0RO2rP2H9mGa1GwrrEGbu0NbS5TPRj1XmVzmBHkJGVdkZKdFcF1u/b2h9TjytIJlyyCvbcFsSZNy8biSWe/dEXmQAH+37q3SuNecjjTVWqf3+7vgvGBzrv3faOmDsUkW0B1hWhZrO/ICwwjgNifEOey0InePOX6UzcrQHWP7hYX83HbTQRNh0h5D0rfSu1FQaaSXpP3HMBlQKuKHwnQbwPmoDK1hdR+B92YPk+YC6kpDHnv5Eg/PY8ZMVwcr2zToDX76TRnUk9WfODZbyIZrz/OYdwd7xBQjYF9ib5xf1hn8xDM0BnbCEHlVfb8YIINPTWy+dOOLKzc37ode0gQ=='
                 }   #11:20
        forecast_response = requests.get(api_url, headers=headers)
        history_response = requests.get(api_call, headers=headers)
        #check the API call is successful or not
        if forecast_response.status_code == 200 and history_response.status_code == 200:

            json_data = forecast_response.json()
            json_result = history_response.json()
            History_list = json_result['response']['jsonDoc']['result']
            Forecast_list = json_data['response']['jsonDoc']['list']
              
            total_temp = 0
            total_humidity = 0
            #Extract the required data from the API response
            for history_entry in History_list:
                mean_temp = history_entry['temp']['mean']
                mean_humidity = history_entry['humidity']['mean']
                total_temp += mean_temp
                total_humidity += mean_humidity
                
            num_entries = len(History_list)    
            meanT = total_temp/num_entries
            meanH = total_humidity/num_entries
            print(meanT) 
            print(meanH)   
            #Extract the required data from the API response
            forecast_data = []
            for forecast_entry in Forecast_list:
                dt = forecast_entry['dt_txt']
                temp = forecast_entry['main']['temp']
                feels_like = forecast_entry['main']['feels_like']
                weather_list = forecast_entry['weather'][0]
                description = weather_list['description']
                main = weather_list['main']
                humidity = forecast_entry['main']['humidity']
                forecast_data.append({
                'dt': dt,
                'temp': temp,
                'humidity': humidity,
                'description': description,
                'feels_like': feels_like,
                'main': main,
                'mean_temp': meanT,
                'mean_humidity': meanH,
            })
                
            recommended_activity = activity_planner(forecast_data)
        

            return JsonResponse({'your_activities': recommended_activity })  
          
        elif forecast_response.status_code != 200:
            error_message = {'error' : 'Something went wrong with forecast API'}
            return JsonResponse(error_message)
        
       
        
        else:
            error_message = {'error' : 'Something went wrong with history API'}
            return JsonResponse(error_message)
        
        