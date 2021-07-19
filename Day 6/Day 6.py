
########################################

# Opening a File

f = open('mbox2.txt')
count = 0

# print(f)
# <_io.TextIOWrapper name='mbox2.txt' mode='r' encoding='cp1252'>


'''
for line in f:
    count += 1
    print(line)
    
print("\n\n\n\n\nTotal Number of lines: ", str(count))
'''
########################################

'''
r = 'X\nY'
print(len(r))  # 3 Because \n is considered a character
'''

########################################

'''
for line in f:
    if line.startswith('From:'):
        print(line[6:].strip())


#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#zqian@umich.edu
'''

########################################

'''
get_file = input('Enter filename: ')


try:
    open_f = open(get_file)
    for i in open_f:
        print(i)
except:
    print("Error! Please type the name correctly.")
'''

########################################
# Writing files


# If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful!
# If the file doesn’t exist, a new one is created.
   
f2 = open('mbox4.txt', 'w')
f2.write("Hala Madrid!")
f2.close()

f3 = open('mbox4.txt', 'r')

for x in f3:
    print(x)
    

'''    
When you are reading and writing files, you might run into problems with whitespace.
These errors can be hard to debug because spaces, tabs, and newlines are normally invisible:
'''
s = '1 2\t 3\n 4'
print(s)

# repr function takes any object as an argument and returns a string representation of the object

print(repr(s))
