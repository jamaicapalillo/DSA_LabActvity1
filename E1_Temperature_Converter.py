# LAB ACTIVITY 1
# Exercise 1:  TEMPERATURE CONVERTER

# Programmed by: Palillo, Jamaica C.
# Section: BSCPE 2-2

# -------------------------------------------

# Instruction: Create a program that converts temperatures between Celsius and Fahrenheit.

# 1. Ask the user to input a temperature.
# 2. Ask the user to select the conversion type: from Celsius to Fahrenheit or from  Fahrenheit to Celsius. 
# 3. Perform the appropriate conversion and print the result.

# -------------------------------------------

# Greetings
print ("Welcome to ThermoTransmute!")

# User's input
print ("Type of Temperature Conversion: ")
print ("\n1. Celsius to Fahrenheit. \n2. Fahrenheit to Celsius")

user_input = int (input("Kindly chooose a type of temperature conversion: "))

if user_input == 1:
    cel_to_far = float (input ("Enter the Temperature in Celsius: "))
    conversion = cel_to_far * 9/5 + 32 #  °F = °C x 9/5 +32 Convert Celsius to Fahrenheit
    print (f"Converted Temperature = {conversion}°F")
elif user_input == 2:
    far_to_cel = float (input ("Enter the Temperature in Fahrenheit: "))
    conversion = 5/9 * (far_to_cel - 32) # # °C = 5/9 (°F-32)
    print (f"Converted Temperature = {conversion}°C")
else:
    print ("Invalid!")




