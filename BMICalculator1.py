
# This program will calculate and print a person's BMI. BMI = kg/m2 where kg is a person's weight and m2 is their height.

# First, we will welcome the user and ask for their height and weight. 


print("Welcome to your personal BMI calculator! Please provide your height in inches.")
height = input()
print("Thank you. Now, please provide your weight in pounds.")
weight = input()
        
# Next, we will convert height to kg and weight to m2.
        
bmiHeight = float(height) / 0.0254
bmiWeight = float(weight) / 0.453592
        
# Here is where we perform the BMI calculation.
        
calcBMI = bmiHeight / bmiWeight
BMI = str(calcBMI)
        
# Finally, we let the user know their BMI output.
        
print (f'Your BMI is {BMI}.')
        
