# BMICalculator.py
# Your job is to write a BMI calculator that matches the formula
# and chart on http://flightphysical.com/medical-exam/weight

# Define Function below
# be sure to return an integer
from decimal import Decimal

class BMICalculator:
    print("BMI Calculator for python using function, simple one.\n")

    # Calculation for BMI
    def CalculateBMI(weight,height):
        total = round((weight / (height/100)**2),2)
        return total

    # This function for choosing our BMI description
    def choose(total):
        if (total < 16):
            print("Severely Underweight")
        elif (total >= 16 and total < 18.5):
            print("Underweight")
        elif (total >= 18.5 and total < 25):
            print("Healthy")
        elif (total >= 25 and total < 30):
            print("Overweight")
        elif (total >= 30):
            print("Severely Overweight")

    # print("Your BMI is : ", round(result, 2))
    # choose(result)
