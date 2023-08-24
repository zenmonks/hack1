from .views1 import WeatherForecast 
from .views2 import WeatherHistory
from django.shortcuts import render
from django.urls import path

def activity_planner():
    forecast = WeatherForecast()
    history = WeatherHistory()

    # Loop 72 times to get 72 hours of data
    for _ in range(72):
        # Check conditions
        if 273 < current_temp < 318 and 273 < feelslike_temp < 320:
            if (mean_temp - 8) < feelslike_temp < (mean_temp + 8):
                result = "Conditions met!"
                if 0 < humidity < 30:
                    result = "dry-humid Conditions!"
                    return result
                if 30 < humidity < 60:
                    result = "moderate-humid Conditions!"
                    return result
                if 60 < humidity < 100:
                    result = "humid Conditions!"
                    return result
            # if humidity & temp satisfy conditions:
               # check for reqiured description & main
                # if description & main satisfy conditions:
                    # return "you can go out"

                #otherwise suggest preventive measures to be taken
                # during heavy rain, thunderstorm, snow, etc. stay indoors

    # If conditions are not met after looping
    result = "Conditions not met after 72 iterations"
    return result



# Call the algorithm with weather data

print(algorithm_result)

