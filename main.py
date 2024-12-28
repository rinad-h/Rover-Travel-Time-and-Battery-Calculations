# Rover Travel Time and Battery Calculations
# This program calculates the total travel time for different rovers based on various parameters
# It also considers the rover's battery power, efficiency, solar capacity, average velocity, 
# and whether a storm is forecasted.

# Define rover parameters
if rover_number == 1:  # Charlie's rover parameters
    battery_power = 100  # Battery power in kWh
    battery_efficiency = 50  # Efficiency in kWh per 100 km
    solar_capacity = 5  # Solar capacity in kW
    average_velocity = 5  # Average velocity in km/h

elif rover_number == 2:  # Alpha's rover parameters
    battery_power = 130
    battery_efficiency = 40
    solar_capacity = 8
    average_velocity = 4

elif rover_number == 3:  # November's rover parameters
    battery_power = 80
    battery_efficiency = 30
    solar_capacity = 4
    average_velocity = 6

else:
    exit('Rover name not recognized')  # If rover number entered is not 1, 2, or 3, the program will exit

# Calculate travel and charging times
travel_time = rover_distance / average_velocity  # Time (hours) = distance (km) / average velocity (km/h)
charge_time = battery_power / solar_capacity  # Time to charge the battery to 100% from 0%
maximum_distance = (100 / battery_efficiency) * battery_power  # Maximum distance per battery cycle
number_rover_stops = rover_distance // maximum_distance  # Number of charging cycles needed
total_time = travel_time + (charge_time * number_rover_stops)  # Total time including charge cycles

# Adjust total time if a storm is forecasted
if storm_forecast:
    total_time *= 1.2  # If storm, multiply total time by 1.2

# Display total travel time
print(f'The total travel time for Rover {rover_number} to travel {rover_distance} km is {round(total_time, 1)} hours.')
