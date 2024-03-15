import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]



min_value = 35
for value in daily_temperatures:
    if value < min_value:
        min_value == value
        print(min_value)