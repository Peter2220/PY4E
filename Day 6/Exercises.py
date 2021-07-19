
# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.

'''
fname = input("Enter a file name: ")

try:
    openFile = open(fname)
    for line in openFile:
        print(line.upper())
except:
    print("Error! Please enter a valid file name.")
'''
########################################

f = input("Enter the file name: ")

lst = []

summ = 0

count = 0

try:
    file = open(f)
    for line in file:
        if line.startswith('X-DSPAM-Confidence: '):
            lst.append(float(line[20:].strip()))
    print(lst)
    
except:
    print("Error opening file! Please enter a valid file name.")
            
for i in range(len(lst)):
    count = count + 1
    summ = summ + lst[i]
    
avg = summ / count
print("Total number of occurances:", str(count))
print("Sum of numbers:", str(summ))
print("Average spam confidence:", str(avg))
