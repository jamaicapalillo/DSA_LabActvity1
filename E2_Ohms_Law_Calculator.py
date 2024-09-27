# LAB ACTIVITY 1
# Exercise 2: OHM'S LAW CALCULATOR

# Programmed by: Palillo, Jamaica C.
# Section: BSCPE 2-2

# -------------------------------------------

# Instruction: 

# 1. Ask the user what they want to calculate: Voltage, Current, or Resistance.
# 2. Based on their choice. prompt the user to input the appropriate values.
# 3. Use Ohm's Law to calculate the missing variable and display the result.
# 4. Handle cases where division by zero might occur.

# -------------------------------------------

# Greetings
print ("Welcome to the Ohm My Watts Calculaotr!!")

# List of things to calculate: Voltage, Current, or Resistance
print ("\nChoose which one of the three you want to calculate: ")
print ("\nV - Voltage \nI - Current \nR - Resistance")

# Ask the user what they want to calculate

while True:

    user_choice = input ("Which one from the three options you want to calculate? ").capitalize()
    
    if user_choice == "V": # Voltage = I * R
            print ("Voltage Calculator! \nVoltage (V) = Current (I) * Resistance (R)")
            current = float(input("Enter Current (I): "))
            resistance = float(input("Enter Resistance (R): "))
            total = current * resistance
            print (f"Voltage (V)= {total:.2f}")
        
    elif user_choice == "I": # Current = V * R
        print ("Current Calculator! \nCurrent (I) = Voltage (V) * Resistance (R)")
        voltage = float(input("Enter Voltage (V): "))
        resistance = float(input("Enter Resistance (R): "))
        total = voltage * resistance
        print (f"Current (I) = {total:.2f}")

    elif user_choice == "R": # Resistance = V/I
        print ("Resistance Calculator! \nResistance (R)= Voltage (V) / Current (I)")
        voltage = float(input("Enter Voltage (V): "))
        current = float(input("Enter Current (I): "))
        total = voltage / current
        print (f"Resistance (R) = {total:.2f}")

    elif user_choice == "Q": 
        print("Exiting the calculator.")
        break

    else:
        print("Invalid choice. Please choose V, I, R, or Q to Quit.")
   
# catch errors inputting value in calculator






# Add loading feature