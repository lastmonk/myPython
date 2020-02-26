# import math


def solve(meal_cost, tip_percent, tax_percent):
    x = meal_cost*(tip_percent/100)
    y = meal_cost*(tax_percent/100)
    z = meal_cost+x+y
    return z


meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())


price = solve(meal_cost, tip_percent, tax_percent)
print(round(price))
