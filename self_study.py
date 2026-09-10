# Variable = A container for storing data values (string, integer, float, boolean, etc.)
#            A varible behaves as if it was the value that it contains.

#Strings
first_name = "Khiem"
food = "Pizza"
email = "khiem@example.com" 

#Integers
age = 22
quantity = 5
num_of_students = 30

#Floats
price = 10.99
gpa = 3.8
distance = 10

#Booleans
is_student = True
for_sale = False

#      print(f"My name is {first_name}")
#      print(f"I am {age} years old")
#      print(f"My email is {email}")
#      print(f"The price of this one is {price} euros")

#      if is_student:
#          print("I am a student")



# Typecasting = Converting a value from one data type to another data type
#              (float, int, str, etc.)
#              str(), int(), float(), bool()

#name = "Khiem"
age = 25
gpa = 3.2
is_student = True

#age = str(age)
# convert age from an integer to a string so that it can be concatenated with another string

#age += "1" 
# += is a shorthand operator that adds the value on the right to the variable on the left and assigns the result back to the variable on the left. In this case, it concatenates "1" to the string representation of age.

#print (age)

given_name = "Khiem"
family_name = ""

#given_name = bool(given_name)
#family_name = bool(family_name)

#print(given_name)
#print(family_name)

# Boolean values are often used in conditional statements to control the flow of a program. 
# In this case, the variable 'given_name' is a non-empty string, so it evaluates to True when converted to a boolean. 
# The variable 'family_name' is an empty string, so it evaluates to False when converted to a boolean.
# In some cases, you may want to check if a string is empty or not, and using boolean values can help with that.



# input() function is a built-in function that allows user input.
# it will return a string value.
name = input("What is your name?: ")
age = input("What is your age?: ")

age = int(age)
age = age + 1

print(f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"You will be {age} years old soon")