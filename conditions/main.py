# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, cows_need_milking, location_of_cows, season, slurry_tank_full, grass_status_long):


    permitted_weather_values = ["rainy", "sunny", "windy", "neutral"]
    permitted_time_of_day_values = ["day", "night"]
    permitted_location_of_cows_values = ["pasture" , "cowshed"]
    permitted_season_values = ["winter" , "spring" , "summer" , "fall"]

    if (weather not in permitted_weather_values):
        return 'wait'
    if (time_of_day not in permitted_time_of_day_values):
        return 'wait'
    if (location_of_cows not in permitted_location_of_cows_values):
        return 'wait'
    if (season not in permitted_season_values):
        return 'wait'    


    if (location_of_cows == 'pasture') and (time_of_day == 'night' or weather == 'rainy'):
        return 'take cows to shed'
        
    elif cows_need_milking == True:
        if location_of_cows == 'cowshed':
            return 'milk cows'
        elif location_of_cows == 'pasture':
            return """take cows to cowshed \nmilk cows \ntake cows back to pasture"""
     
    elif ( slurry_tank_full == True and (weather == 'rainy' or weather == 'neutral')):
        if location_of_cows == 'cowshed':
            return 'fertilize pasture' 
        elif location_of_cows == 'pasture':
            return """take cows to cowshed
                      fertilize pasture
                      take cows back to pasture"""

    elif grass_status_long == True and season == 'spring' and weather == 'sunny':
        print('3')
        if location_of_cows == 'cowshed':
            return 'mow grass'    
        elif location_of_cows == 'pasture':
            return """take cows to cowshed
                      mow grass
                      take cows back to pasture"""    
    else:
        return 'wait'


result1 = farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
print(result1)
#'fertilize pasture'

result2 = farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
print(result2)
#'wait'

result3 = farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
print(result3)
#'milk cows'

#2do: fix below:
result4 = farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
print(result4)
"""take cows to cowshed
milk cows
take cows back to pasture"""



# 2do: debug with code below: 
# def farm_action(weather, time_of_day, milking_status, cow_location, season, slurry_tank, grass_status):
#     if cow_location == "pasture" and (time_of_day == "night" or weather == "rainy"):
#        action = "take cows to the cowshed"

#     elif milking_status == True:
#         if cow_location == "cowshed":
#            action = "milk cows"

#         elif cow_location == "pasture":
#             action = "take cows to cowshed\nmilk cows\ntake cows back to pasture"

#     elif slurry_tank == True and weather != "sunny" and weather != "windy":
#         if cow_location == "cowshed":
#             action = "fertilize pasture"

#         else:
#             action = "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"

#     elif grass_status == True and season == "spring" and weather == "sunny":
#         if cow_location == "cowshed":
#             action = "mow grass"

#         else:
#             action = "take cows to cowshed\nmow grass\ntake cows back to pasture"

#     else:
#         action = "wait"

#     return action