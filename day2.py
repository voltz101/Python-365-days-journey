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

###using strip() method to remove any leading or trailing whitespace from the string.
first_name=input("What is your first name? ")
last_name=input("What is your last name? ") 
first_name=first_name.strip()
last_name=last_name.strip()     
full_name=f"{first_name.title()} {last_name.title()}"
print(f"Hello, {full_name}! Welcome to Python programming.")    
#using /t amd /n to add a tab and a new line in the string.


print("Hello, \tWorld!")  #adds a tab before the word "World"
print("Hello, \nWorld!")  #adds a new line before the word "World"  

#using rstrip() method to remove any trailing whitespace from the string.
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")
first_name=first_name.rstrip()
last_name=last_name.rstrip()
full_name=f"{first_name.title()} {last_name.title()}"
print(f"Hello, {full_name}! Welcome to Python programming.")

#using lstrip() method to remove any leading whitespace from the string.
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")
first_name=first_name.lstrip()
last_name=last_name.lstrip()
full_name=f"{first_name.title()} {last_name.title()}"
print(f"Hello, {full_name}! Welcome to Python programming.")

#removing prefixesand suffixes from a string using the removeprefix() and removesuffix() methods.
filename="python_tutorial.txt"
print(filename.removeprefix("python_"))  #removes the prefix "python_"  
print(filename.removesuffix(".txt"))  #removes the suffix ".txt"

nostarchurl="https://nostarch.com"
print(nostarchurl.removeprefix("https://"))  #removes the prefix "https://"
print(nostarchurl.removesuffix(".com"))  #removes the suffix ".com"

name="Suman Subedi"
print(name.removeprefix("Suman"))  #removes the prefix "Suman"
print(name.removesuffix("Subedi"))  #removes the suffix "Subedi"

# try it yourself from the book "Python Crash Course" by Eric Matthes-personal message to the user using f-string and title() method to greet the user.
user_name=input("What's your Username: ")
Real_user_name=f"{user_name.title()}"
print(f"Hello, {Real_user_name}! Welcome to the Python Practice Course! I am absolutely thrilled to have you here.Whether you are looking to automate boring tasks, dive into data science, or build your very first app, you’ve taken a massive step toward making it happen. Python is famous for being friendly to learn, but the real secret to mastering it isn't just reading tutorials—it's writing code. That is exactly what we are going to do here.")

# try it yourself from the book "Python Crash Course" by Eric Matthes-name cases-using upper() method to convert the string to uppercase,lowercase, and title() method to capitalize the first letter of each word in the string.
first_name=input("What's your First Name? ")
last_name=input("What's your Last Name? ")
full_name=f"{first_name.title()} {last_name.title()}"
print(full_name)
print(full_name.upper())
print(full_name.lower())

#try it yourself from the book "Python Crash Course" by Eric Matthes-famous quote-using f-string to format the string and include a famous quote.
famous_person="gandhi"
quote="Be the change that you wish to see in the world."
message=f'{famous_person.title()} once said ,"{quote}"'
print(message)


#try it yourself from the book "Python Crash Course" by Eric Matthes-striping names-using strip() method to remove any leading or trailing whitespace from the string first add whitespace using the /t and /n characters and then remove it using the strip() method.
first_name=input("What's your First Name? ")
last_name=input("What's your Last Name? ")
full_name=f"{first_name.title()} {last_name.title()}"
print(f"\t{full_name}\n")  
full_name_s=f"\t{first_name.title()}\n {last_name.title()}\t"
print(full_name_s)  #prints the full name with a tab between the first and last name

print(full_name.lstrip())  #removes the leading whitespace from the full name
print(full_name.rstrip())  #removes the trailing whitespace from the full name
print(full_name.strip())  #removes the leading and trailing whitespace from the full name




