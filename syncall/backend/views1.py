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
           geocoding_api_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zipCode},{countryCode}&appid=your_api_key'
        
        geocoding_response = requests.get(geocoding_api_url)
        geocoding_data = geocoding_response.json()
        
        lat = geocoding_data['lat']
        lon = geocoding_data['lon']
        
        #Get the weather forecast from the API
        api_url = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiapp.weather.weatherforecast.main?lat={lat}&lon={lon}'
        api_call = f'https://cloud.syncloop.com/tenant/1692162910856/packages.apiweather.weatherii.weatherhistory.main?lat={lat}&lon={lon}'
        headers = { 
                    'Content-Type' : 'application/json',
                    'Authorization' : 'Bearer {token}'
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
        

            return render(request,'output.html', {'your_activities': recommended_activity })  
          
        elif forecast_response.status_code != 200:
            error_message = {'error' : 'Something went wrong with forecast API'}
            return JsonResponse(error_message)
        
       
        
        else:
            error_message = {'error' : 'Something went wrong with history API'}
            return JsonResponse(error_message)
        
        