for character in 'banana':
    print(character)

########################################

# Slicing

'''
s = 'Federico Chiesa'

f = '   Iker Casillas'
print(s[:])
print(s[0:4]) # Fede

'm' in s # False
'e' in s # True


s.lower()     # federico chiesa
s.upper()     # FEDERICO CHIESA
s.find('ico') # 5
s.replace("Federico", "Ramos") # Ramos Chiesa
f.lstrip() # Iker Casillas
# f.rstrip()
# f.strip
'''

########################################

'''
greeting = 'Hello, world!'
greeting[0] = 'J'

TypeError: 'str' object does not support item assignment
'''

'''
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)
Jello, world!
'''

########################################

'''
Available methods for s string

>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', ...]

'''

########################################

# Exercise 1
'''
def count_letter(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count = count + 1
    print(count)
'''

########################################

# Format operator

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# https://www.w3schools.com/python/ref_string_format.asp

########################################

text = 'X-DSPAM-Confidence:0.8475'

colon_index = text.find(':')
str_to_float = float(text[colon_index + 1:])

print(type(str_to_float))
