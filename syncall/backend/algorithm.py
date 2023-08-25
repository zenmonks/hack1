import json
from .views1 import WeatherForecast 
from .views2 import WeatherHistory
from django.shortcuts import render
from django.urls import path

def activity_planner(weather_data, weather_history):
    forecast = WeatherForecast()
    history = WeatherHistory()

    #get the mean-values for that location
    mean_temp = weather_history['mean_temp']
    
    weather_description = "heavy intensity rain"  # Replace with the actual weather description

    # Get the weather parsed_data from views1.py & views2.py 
    for entry in weather_data:
        # Check conditions
        if 273 < entry['temp'] < 318 and 260 < entry['feels_like'] < 320:
            if (mean_temp - 7) < entry['feels_like'] < (mean_temp + 7):

                if "Thunderstorm" in main:
                    weather_description = "thunderstorm with heavy rain"  # Replace with the actual weather description
                    if "thunderstorm with heavy rain" in weather_description:
                        door = 'indoor'
                        tip = 'unplug electronics'
                        return door, tip
                    elif "thunderstorm with light rain" in weather_description:
                        door = 'indoor' 
                        tip = 'stay away from open areas and tall objects'
                        return door, tip
                    elif "thunderstorm with rain" in weather_description:
                        door = 'indoor'
                        tip = 'stay away from open areas and tall objects'
                        return door, tip
                    elif "light thunderstorm" in weather_description:
                        door = 'indoor'
                        tip = 'stay away from open areas and tall objects'
                        return door, tip
                    elif "heavy thunderstorm" in weather_description:
                        door = 'indoor'
                        tip = 'unplug electronics'
                        return door, tip
                    elif "ragged thunderstorm" in weather_description:
                        door = 'indoor' 
                        tip = 'stay away from open areas and tall objects'
                        return door, tip
                    elif "thunderstorm" in weather_description:
                        door = 'outdoor'
                        tip = 'go with precautions'
                        return door, tip
                    elif "thunderstorm with light drizzle" in weather_description:
                        door = 'outdoor' 
                        tip = 'Be caution about lightning'
                        return door, tip
                    elif "thunderstorm with drizzle" in weather_description:
                        door = 'indoor'
                        tip = 'go out with precautions'
                        return door, tip
                    elif "thunderstorm with heavy drizzle" in weather_description:
                       door = 'indoor'
                       tip = 'go out with precautions'
                       return door, tip
                       

                elif "Drizzle" in main:
                    if "heavy intensity drizzle rain" in weather_description:
                        door = 'indoor & go out with umbrella/raincoat'("It's better to stay indoors during heavy intensity drizzle rain.")
                        return door
                    elif "light intensity drizzle rain" in weather_description:
                        door = 'outdoor & keep an umbrella or raincoat'
                        return door
                    elif "drizzle rain" in weather_description:
                        door = 'outdoor & keep an umbrella or raincoat'
                        return door
                    elif "heavy intensity drizzle" in weather_description:
                        door = 'indoor & go out with umbrella/raincoat'
                        return door
                    elif "light intensity drizzle" in weather_description:
                        door = 'outdoor & keep an umbrella or raincoat'
                        return door
                    elif "shower rain and drizzle" in weather_description or "heavy shower rain and drizzle" in weather_description:
                        door = 'indoor & go out with umbrella/raincoat'
                        return door
                    elif "shower drizzle" in weather_description:
                        door = 'outdoor & keep an umbrella or raincoat'
                        return door

                elif "Rain" in main:
                    if "Extreme rain" in weather_description:
                        door = 'indoor & stay away from flood-prone areas'
                        return door
                    elif "Very heavy rain" in weather_description:
                        door = 'indoor & stay away from rivers, low-lying areas'
                        return door
                    elif "Heavy intensity rain" in weather_description:
                        door = 'indoor & keep an umbrella or raincoat'
                        return door
                    elif "Moderate rain" in weather_description:
                        door = 'indoor & keep an umbrella or raincoat'
                        return door
                    elif "Light intensity rain" in weather_description:
                        door = 'outdoor & keep an umbrella or raincoat'
                        return door
                    elif "Light intensity shower rain" in weather_description:
                        door = 'outdoor & keep an umbrella or raincoat'
                        return door
                    elif "Shower rain" in weather_description:
                        door = 'indoor & keep an umbrella or raincoat'
                    elif "Heavy intensity shower rain" in weather_description:
                        door = 'indoor & keep an umbrella or raincoat'
                        return door
                    elif "Ragged shower rain" in weather_description:
                        door = 'indoor & keep an umbrella or raincoat'
                        return door
                    elif "Freezing rain" in weather_description:
                        door = 'indoor & avoid driving on icy roads'
                        return door

                elif "Snow" in main:
                    if "Heavy snow" in weather_description:
                        door = 'indoor & avoid unnecessary travel'
                        
                    elif "Light snow" in weather_description:
                        door = 'outdoor & dress warmly, avoid icy areas'
                        
                    elif "snow" in weather_description:
                        door = 'indoor & avoid unnecessary travel'
                        
                    elif "Sleet" in weather_description:
                        door = 'indoor & avoid unnecessary travel'
                        
                    elif "Rain and snow" in weather_description:
                        door = 'indoor'
                        tip = 'Avoid unnecessary travel.'
                        return door, tip
                    elif "Shower snow" in weather_description:
                        door = 'indoor'
                        tip = 'Avoid unnecessary travel'
                        return door, tip
                    elif "Light shower sleet" in weather_description:
                        door = 'indoor'
                        tip = 'Dress warmly and avoid slippery areas.'
                        return door, tip
                    elif "Shower sleet" in weather_description:
                        door = 'indoor'
                        tip = 'Avoid outdoor activities, as it can be hazardous.'
                        return door, tip
                    elif "Light rain and snow" in weather_description:
                        door = 'indoor'
                        tip = 'Dress in layers and keep an umbrella.'
                        return door, tip
                    elif "Light shower snow" in weather_description:
                        door = 'indoor'
                        tip = 'avoid unnecessary travel'
                        return door, tip
                    elif "Heavy shower snow" in weather_description:
                        door = 'indoor'
                        tip = 'avoid unnecessary travel'
                        return door, tip

                elif "Atmosphere" in main:
                    if "Mist" in weather_description:
                        door = 'outdoor'
                        tip = 'Drive carefully'
                        return door, tip
                    elif "Smoke" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        return door, tip
                    elif "Haze" in weather_description:
                        door = 'outdoor'
                        tip = 'Drive carefully'
                        return door, tip
                    elif "Sand/dust whirls" in weather_description:
                        door = 'indoor'
                        tip = 'close windows and doors, and cover your face if needed.'
                        return door, tip
                    elif "Fog" in weather_description:
                        door = 'outdoor'
                        tip = 'Drive carefully'
                        return door, tip
                    elif "Sand" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        return door, tip
                    elif "Dust" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        return door, tip
                    elif "Volcanic ash" in weather_description:
                        door = 'indoor'
                        tip ='use air purifiers if available.'
                        return door, tip
                    elif "Squalls" in weather_description:
                        door = 'indoor'
                        tip = 'Secure outdoor objects, close windows and doors securely.'
                        return door, tip
                    elif "Tornado" in weather_description:
                        door = 'indoor'
                        tip = 'Move to a basement or an interior room, away from windows.'
                        return door, tip
                    
                elif "Clear" in main:
                    if "Clear sky" in weather_description:
                        door = 'outdoor'
                        tip = 'Wear sunscreen and sunglasses, and stay hydrated.'
                        return door, tip
                    
                elif "Clouds" in  main:
                    if "few clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Wear sunscreen and stay hydrated.'
                        return door, tip
                    elif "scattered clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Wear sunglasses and stay hydrated.'
                        return door, tip
                    elif "broken clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Keep an umbrella handy and stay aware of changing weather.'
                        return door, tip
                    elif "overcast clouds" in weather_description:
                        door = 'outdoor'
                        tip = 'Be prepared for possible rain.'
                        return door, tip

            elif entry['feels_like'] > 318 or entry['feels_like'] < 260:
                #feels-like temperature is not so good
                door = 'indoor'
                tip = 'Stay hydrated and avoid outdoor activities.'
                return door, tip
            elif entry['feels_like'] < (mean_temp - 7) or entry['feels_like'] > (mean_temp + 7):
                door = 'indoor'
                tip = 'Stay hydrated and avoid outdoor activities.'
                return door, tip
        else:
            return "temparature is not suitable for humans"
        
        
        #
    # If conditions are not met after looping
    result = "Conditions not met after 72 iterations"
    return result



# Call the algorithm with weather data

print(algorithm_result)

