# Compare two numbers
"""
x = int(input("Enter the First number: "))
y = int(input("Enter the Second number: "))

if x < y:
    print('X is less than Y')
elif x > y:
    print('X is greater than Y')
else:
    print('X and Y are equal')
"""

# Try Execpt (catching errors)
"""
inp = input('Enter Fahrenheit Temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
"""

####################################################

"""
Exercise 1: Rewrite your pay computation to give the employee
1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    pay = (hours * rate) + (0.5 * rate * (hours - 40)) 
    print("Pay:", str(pay))
"""

####################################################

"""
Exercise 2: Rewrite your pay program using try and except so that
your program handles non-numeric input gracefully by printing
a message and exiting the program.

####################################################
hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

try:
    hrs = float(hours)
    ra = float(rate)
    if hrs > 40:
        pay = (hrs * ra) + (0.5 * ra * (hrs - 40))
        print("Pay:", str(pay))
except:
    print("Error, please enter numeric input!")
"""

####################################################

"""
Exercise 4: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
If the score is between 0.0 and 1.0, print a grade using the following table:
 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
"""

prompt = input("Enter score between 0.0 and 1.0: ")

try:
    score = float(prompt)
    if score <= 1.0:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("\nEnter score between 0.0 and 1.0\n")
except:
    print("\nBad Score!\n")


    
