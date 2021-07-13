'''
n = 5

while n > 0:

    print(n)
    n = n - 1

print("Blow up!")
print(n)
'''

########################################

'''
lst = [5, 4, 3, 2, 1]
for i in lst:
    print(i)
'''

########################################

'''

summ = 0
count = 0

lst = [5, 2, 3, 4, 5, 8]

for i in lst:
    count = count + 1
    summ = summ + i
    print("Count:", count, " &  Sum:", summ, "\n")
    
print("\nTotal count:", str(count) + "\n")
print("Total sum:", summ)

'''

########################################

# Finding the smallest value using (None)

'''
smallest = None
print('Before the loop!\n')

for i in [50, 30, 2, 38, 97, 74, 15]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i

    print("Smallest value:", smallest, " & Current Value:", i, "\n")


print("Smallest number after executing the loop:", smallest)
'''

########################################

# Suppose you want to take input from the user until they type done
'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


If the user types done, the break statement exits the loop.
Otherwise the program echoes whatever the user types and goes back to the top of the loop.
'''

########################################

# Finishing iterations with continue

'''
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)

print('Done!')
'''

########################################

# Definite loops using for

'''
players_lst = ['Ramos', 'Modric', 'Isco', 'Casillas']

for player in players_lst:
    print("Real Madrid player:", player)
'''

########################################
    
# Maximum and minimum loops

# To find the largest value in a list or sequence, we construct the following loop:

# None is a special constant value which we can store in a variable to mark the variable as “empty”.
'''
largest = None

nums = [50, 2, 7, 55, 36, 47, 80, 99]

for i in nums:
    if largest is None or i > largest:
        largest = i
    print('Current number in the Loop:', i, ' & Current largest number:', largest)

print("\n\nLargest number in the list is: " + str(largest))
'''

########################################

# Ecercise 1 & 2
summ = 0
count = 0
lst = []
avg = 0

hello_msg = print("Enter a number or 'done' to exit.\n")
while True:
    hello_msg
    line = input("> ")
    if line == 'done':
        break
    else:
        try:
            int(line)
            count = count + 1
            lst.append(int(line))
        except:
            print("\nError! Please enter a number.\n")
        
for i in range(len(lst)):
    summ = summ + lst[i]
    avg = summ / len(lst)

print("\nList contains the following numbers:", *lst)
print("\nCount: " + str(count))
print("\nSum: " + str(summ))
print("\nAverage: " + str(avg))
print("\nMaximum number in the list:", max(lst))
print("\nMinimum number in the list:", min(lst))
