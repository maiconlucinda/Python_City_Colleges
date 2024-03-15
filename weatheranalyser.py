import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]
print(daily_temperatures)

#Using this list of daily temperatures, write separate for-loops to do the following. You can use the enumerate method in the for-loop statement to keep track of the days.

# • Find the day with the lowest temperature.
min_temperature = float('inf')

for day, temperature in enumerate(daily_temperatures, start = 1):
    if temperature < min_temperature:
        min_temperature = temperature
        min_temp_day = day
    
print(f"The lowest temperature was: {min_temperature}°, occurred on day {min_temp_day}")
        



# • Find the day with the highest temperature.
max_temperature = float('-inf')

for day, temperature in enumerate(daily_temperatures, start = 1):
    if temperature > max_temperature:
        max_temperature = temperature
        max_temp_day = day
    
print(f"The highest temperature was: {max_temperature}°, occurred on day {max_temp_day}")




# • Find the days where the temperature rises above 20°C.
max_temperature = []
max_temp_day = []
above_twenty = 20

for day, temperature in enumerate(daily_temperatures, start = 1):
    if temperature > above_twenty:
        max_temperature.append(temperature)
        max_temp_day.append(day)

for value1, value2 in zip(max_temp_day, max_temperature):
    print(f"Day: {value1} the temprature was above 20: {value2}")





# • Find the days where the temperature drops below 10°C.
min_temperature = []
min_temp_day = []
below_ten = 10

for day, temperature in enumerate(daily_temperatures, start = 1):
    if temperature < below_ten:
        min_temperature.append(temperature)
        min_temp_day.append(day)

for value1, value2 in zip(min_temp_day, min_temperature):
    print(f"Day: {value1} the temprature was below 10: {value2}")





# • Find the days where the temperature increased from the day before.
increased_temperature_days = []

for day in range(1, len(daily_temperatures)):
    if daily_temperatures[day] > daily_temperatures[day - 1]:
        increased_temperature_days.append(day + 1) 

print("Days where temperature increased from the previous day:", increased_temperature_days)





# • Find the days where the temperature was hotter than any of the days previous in the month.
max_temp_up_to_day = daily_temperatures[0] 
hotter_than_previous_days = []


for day in range(1, len(daily_temperatures)):
    if daily_temperatures[day] > max_temp_up_to_day:
        hotter_than_previous_days.append(day + 1)  
        max_temp_up_to_day = daily_temperatures[day]
    else:
        max_temp_up_to_day = max(max_temp_up_to_day, daily_temperatures[day])

print("Days where temperature was hotter than any of the previous days:", hotter_than_previous_days)