import random as rd

# Generate random numbers
'''
for i in range(5):
    x = rd.random()       # Random numbers (float) between 0.0 and 1.0
    y = rd.randint(5, 10) # Random numbers (integer) between 5 and 10
    print("Random number X: ", str(x), "\nRandom number Y: ", str(y))
    

def random_text():
    print("\nHello World!")
    print("\nWelcome to Spain!")

random_text()
'''

################################################################

'''
Exercise 1: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters
'''

def computepay(hours, rate):
    pay = (hours * rate) + 0.5 * (hours - 40) * rate
    print(pay)

################################################################
'''
Exercise 2: Rewrite the grade program from the previous chapter using a function called
computegrade that takes a score as its parameter and returns a grade as a string.
'''

def computegrade(score):
    if score < 1.0:
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


