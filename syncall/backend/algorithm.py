import json
from django.shortcuts import render
from django.urls import path

def activity_planner(forecast_data):
    suggest = []
    # Get the weather parsed_data from views1.py & views2.py   
    for entry in forecast_data:
        time = entry['dt'] 
        main = entry['main']
        weather_description = entry['description'] 
        mean_temp = entry['mean_temp']
        if 273 < entry['temp'] < 318 and 260 < entry['feels_like'] < 320:
             
            if (mean_temp - 9) < entry['feels_like'] < (mean_temp + 9):
                
                if "Thunderstorm" in main: 
                    if "thunderstorm with heavy rain" in weather_description:
                        door = 'indoor'
                        tip = 'unplug electronics'
                        suggest.append((door, tip, time))
                    elif "thunderstorm with light rain" in weather_description:
                        door = 'indoor' 
                        tip = 'stay away from open areas and tall objects'
                        suggest.append((door, tip, time))
                    elif "thunderstorm with rain" in weather_description:
                        door = 'indoor'
                        tip = 'stay away from open areas and tall objects'
                        suggest.append((door, tip, time))
                    elif "light thunderstorm" in weather_description:
                        door = 'indoor'
                        tip = 'stay away from open areas and tall objects'
                        suggest.append((door, tip, time))
                    elif "heavy thunderstorm" in weather_description:
                        door = 'indoor'
                        tip = 'unplug electronics'
                        suggest.append((door, tip, time))
                    elif "ragged thunderstorm" in weather_description:
                        door = 'indoor' 
                        tip = 'stay away from open areas and tall objects'
                        suggest.append((door, tip, time))
                    elif "thunderstorm" in weather_description:
                        door = 'outdoor'
                        tip = 'go with precautions'
                        suggest.append((door, tip, time))
                    elif "thunderstorm with light drizzle" in weather_description:
                        door = 'outdoor' 
                        tip = 'Be caution about lightning'
                        suggest.append((door, tip, time))
                    elif "thunderstorm with drizzle" in weather_description:
                        door = 'indoor'
                        tip = 'go out with precautions'
                        suggest.append((door, tip, time))
                    elif "thunderstorm with heavy drizzle" in weather_description:
                       door = 'indoor'
                       tip = 'go out with precautions'
                       suggest.append((door, tip, time))
                       
                elif "Drizzle" in main:
                    if "heavy intensity drizzle rain" in weather_description:
                        door = 'indoor'
                        tip = 'go out with umbrella/raincoat'
                        suggest.append((door, tip, time))
                    elif "light intensity drizzle rain" in weather_description:
                        door = 'outdoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "drizzle rain" in weather_description:
                        door = 'outdoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "heavy intensity drizzle" in weather_description:
                        door = 'indoor'
                        tip = 'go out with umbrella/raincoat'
                        suggest.append((door, tip, time))
                    elif "light intensity drizzle" in weather_description:
                        door = 'outdoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "shower rain and drizzle" in weather_description or "heavy shower rain and drizzle" in weather_description:
                        door = 'indoor' 
                        tip = 'go out with umbrella/raincoat'
                        suggest.append((door, tip, time))
                    elif "shower drizzle" in weather_description:
                        door = 'outdoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))

                elif "Rain" in main:
                    if "Extreme rain" in weather_description:
                        door = 'indoor'
                        tip = 'stay away from flood-prone areas'
                        suggest.append((door, tip, time))
                    elif "Very heavy rain" in weather_description:
                        door = 'indoor' 
                        tip = 'stay away from rivers, low-lying areas'
                        suggest.append((door, tip, time))
                    elif "Heavy intensity rain" in weather_description:
                        door = 'indoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Moderate rain" in weather_description:
                        door = 'indoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Light intensity rain" in weather_description:
                        door = 'outdoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Light intensity shower rain" in weather_description:
                        door = 'outdoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Shower rain" in weather_description:
                        door = 'indoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Heavy intensity shower rain" in weather_description:
                        door = 'indoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Ragged shower rain" in weather_description:
                        door = 'indoor'
                        tip = 'keep an umbrella or raincoat'
                        suggest.append((door, tip, time))
                    elif "Freezing rain" in weather_description:
                        door = 'indoor'
                        tip = 'avoid driving on icy roads'
                        suggest.append((door, tip, time)) 

                elif "Snow" in main:
                    if "Heavy snow" in weather_description:
                        door = 'indoor' 
                        tip = 'avoid unnecessary travel'
                        suggest.append((door, tip, time))
                    elif "Light snow" in weather_description:
                        door = 'outdoor'
                        tip = 'dress warmly, avoid icy areas'
                        suggest.append((door, tip, time))
                    elif "snow" in weather_description:
                        door = 'indoor'
                        tip = 'avoid unnecessary travel'
                        suggest.append((door, tip, time))
                    elif "Sleet" in weather_description:
                        door = 'indoor'
                        tip = 'avoid unnecessary travel'
                        suggest.append((door, tip, time))
                    elif "Rain and snow" in weather_description:
                        door = 'indoor'
                        tip = 'Avoid unnecessary travel.'
                        suggest.append((door, tip, time))
                    elif "Shower snow" in weather_description:
                        door = 'indoor'
                        tip = 'Avoid unnecessary travel'
                        suggest.append((door, tip, time))
                    elif "Light shower sleet" in weather_description:
                        door = 'indoor'
                        tip = 'Dress warmly and avoid slippery areas.'
                        suggest.append((door, tip, time))
                    elif "Shower sleet" in weather_description:
                        door = 'indoor'
                        tip = 'Avoid outdoor activities, as it can be hazardous.'
                        suggest.append((door, tip, time))
                    elif "Light rain and snow" in weather_description:
                        door = 'indoor'
                        tip = 'Dress in layers and keep an umbrella.'
                        suggest.append((door, tip, time))
                    elif "Light shower snow" in weather_description:
                        door = 'indoor'
                        tip = 'avoid unnecessary travel'
                        suggest.append((door, tip, time))
                    elif "Heavy shower snow" in weather_description:
                        door = 'indoor'
                        tip = 'avoid unnecessary travel'
                        suggest.append((door, tip, time))

                elif "Atmosphere" in main:
                    if "Mist" in weather_description:
                        door = 'outdoor'
                        tip = 'Drive carefully'
                        suggest.append((door, tip, time))
                    elif "Smoke" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        suggest.append((door, tip, time))
                    elif "Haze" in weather_description:
                        door = 'outdoor'
                        tip = 'Drive carefully'
                        suggest.append((door, tip, time))
                    elif "Sand/dust whirls" in weather_description:
                        door = 'indoor'
                        tip = 'close windows and doors, and cover your face if needed.'
                        suggest.append((door, tip, time))
                    elif "Fog" in weather_description:
                        door = 'outdoor'
                        tip = 'Drive carefully'
                        suggest.append((door, tip, time))
                    elif "Sand" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        suggest.append((door, tip, time))
                    elif "Dust" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        suggest.append((door, tip, time))
                    elif "Volcanic ash" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        suggest.append((door, tip, time))
                    elif "Squalls" in weather_description:
                        door = 'indoor'
                        tip = 'Secure outdoor objects, close windows and doors securely.'
                        suggest.append((door, tip, time))
                    elif "Tornado" in weather_description:
                        door = 'indoor'
                        tip = 'Move to a basement or an interior room, away from windows.'
                        suggest.append((door, tip, time))
                    
                elif "Clear" in main:
                    if "Clear sky" in weather_description:
                        door = 'outdoor'
                        tip = 'Wear sunscreen and sunglasses, and stay hydrated.'
                        suggest.append((door, tip, time))
                    
                elif "Clouds" in  main:
                    if "few clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Wear sunscreen and stay hydrated.'
                        suggest.append((door, tip, time))
                    elif "scattered clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Wear sunglasses and stay hydrated.'
                        suggest.append((door, tip, time))
                    elif "broken clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Keep an umbrella handy and stay aware of changing weather.'
                        suggest.append((door, tip, time))
                    elif "overcast clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Be prepared for possible rain.'
                        suggest.append((door, tip, time))

            elif entry['feels_like'] > 318 or entry['feels_like'] < 260:
                #feels-like temperature is not so good
                door = 'indoor'
                tip = 'Stay hydrated and avoid outdoor activities.'
                suggest.append((door, tip, time))
            
            elif entry['feels_like'] < (mean_temp - 9) or entry['feels_like'] > (mean_temp + 9):
                door = 'indoor'
                tip = 'Stay hydrated and avoid outdoor activities.'
                suggest.append((door, tip, time))
       
        else:
            return ("temparature is not suitable for humans")
        
    return suggest