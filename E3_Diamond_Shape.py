# LAB ACTIVITY 1
# Exercise 3: DIAMOND SHAPE 

# Programmed by: Palillo, Jamaica C.
# Section: BSCPE 2-2

# -------------------------------------------

# Instruction: 

# Write a Python fucntioin named print_diamond that takes an odd integer n as argument 
# and prints a diamond shape with a width of n using the * character.

# -------------------------------------------

def print_diamond():
    while True:
        try:
            n = int(input("Enter an odd integer for the diamond shape: "))
            if n % 2 == 0:
                print("The number must be an odd integer. Please try again.")
            else:
                break  # Exit the loop when a valid odd integer is entered
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

    for i in range(n // 2 - 1, -1, -1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))


print_diamond()



