import math

sum_arr_one = []
sum_arr_two = []

file = open("day1-input.txt", "r")
lines = file.readlines()

def how_much_fuel(mass):
    return int(math.floor(int(mass)/3)-2)

def rec_sum(mass):
    fuel_mass = how_much_fuel(mass)
    return (fuel_mass + rec_sum(fuel_mass)) if fuel_mass >= 0 else 0

for line in lines:
    sum_arr_one.append(how_much_fuel(int(line)))
    sum_arr_two.append(rec_sum(int(line)))

print("Part 1: " + str(sum(sum_arr_one)))
print("Part 2: " + str(sum(sum_arr_two)))