# string data type

# literal assignment
import math


first = "James"
last = "Ngunga"

# print(type(first))
# print(type(first)== str)
# print(isinstance(first, str))

# #constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza)== str)
# print(isinstance(pizza, str))

#concatenation
full_name = first + " " + last
print(full_name)

full_name = first + " " + last + " is a good boy"
print(full_name)

#casting a number to a string
decade = str(1999)
print(type(decade))
print(decade)

statement = "I like football from the "+ decade + "s"
print(statement)


# Multiple-lines
multi_line = '''
hey, how are you?

i was just checking in.
                             All good?

'''
print(multi_line)

#escape special characters
sentence = 'I\'m back at work!\tHey!\n\n Where\'s this at \\located?'
print(sentence)

#string methods

print(first)
print(first.lower())
print(first.upper())
print(first.title())

print(multi_line.strip())
print(multi_line.replace("good", "great"))
print(multi_line)

print(len(multi_line))
multi_line += "                                "
multi_line = "        " + multi_line
print(len(multi_line))

print(len(multi_line.strip()))
print(len(multi_line.lstrip()))
print(len(multi_line.rstrip()))
print(len(multi_line.rstrip()))


#build a menu
#build a menu
title = "Menu" . upper()
title = "Menu" . upper()
print(title.center(20, "="))
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$2.50".rjust(4))
print("coffee".ljust(16, ".") + "$2.50".rjust(4))
print("muffin".ljust(16, ".") + "$4.50".rjust(4))
print("muffin".ljust(16, ".") + "$4.50".rjust(4))
print("cheesecake".ljust(16, ".") + "$4.50".rjust(4))
print("cheesecake".ljust(16, ".") + "$4.50".rjust(4))


# string index values
# string index values
print(first[1])
print(first[-1])
print(first[1:])
print(first[1])

#some methods return boolen data

print(first.startswith("J"))
print(first.endswith("s"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data types

# integer data type
Price = 100
best_price = int(99.99)
print(type(Price))
print(isinstance(best_price, int))

#float data type
gpa = 3.5
y=float(3)
print(type(gpa))

#complex data type
comp_Value = 2 + 3j
print(type(comp_Value))
print(comp_Value.real)
print(comp_Value.imag)

#built-in functions
print(abs(gpa))
print(abs(gpa * -1))


print(round(gpa))
print(round(gpa, 1))

import math 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


#casting a string to a number
zipcode = "90210"
zip_value = int(zipcode)
print(type(zip_value))

#Error if you attampt to cast incorrect data
# zipcode = Int("New York")