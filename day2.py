#variables Continued 

#types of variables #sting, int, float, bool

#string is a sequence of characters, it can be letters, numbers, or symbols. It is enclosed in quotes, either single or double.

#int is a whole number, it can be positive or negative, but it cannot have a decimal point.

#float is a number that can have a decimal point, it can be positive or negative.   

#bool is a data type that can only have two values: True or False. It is used to represent the truth value of an expression.

#example of string

name="  Suman Subedi"
print(name)

#title() method capitalizes the first letter of each word in the strring

name="suman subedi"
print(name.title()) 

#using any quotation mark to represent a string

message='I am learning Python.'
print(message)

message="I am learning Python."
print(message)  

#using different quotation helps to avoid syntax error and express the true meaning of the string message.

message="I am learning Python. It's really fun!"
print(message)

#using backslash to escape the single quote in the string

message='I am learning Python. It\'s really fun!'
print(message)

#using upper() method to convert the string to uppercase
#using lower() method to convert the string to lowercase

message="I am learning Python."
print(message.upper())  
print(message.lower())

message="my name is suman subedi."
print(message.title())  
print(message.upper())
print(message.lower())

#f-strings are a way to format strings in Python. They are prefixed with the letter 'f' and allow you to include variables and expressions inside the string using curly braces {}.
first_name="Suman"
last_name="Subedi"
full_name=f"{first_name} {last_name}"
print(full_name)        

#using title() method to capitalize the first letter of each word in the string along with f-string.
first_name="suman"
last_name="subedi"
full_name=f"{first_name.title()} {last_name.title()}"
print(full_name)

# making the user input their name and using f-string to greet the user.
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")     
full_name=f"{first_name.title()} {last_name.title()}"
print(f"Hello, {full_name}! Welcome to Python programming.")


