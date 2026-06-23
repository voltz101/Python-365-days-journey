#Variables numbers(Integersand floats) and basic arithmetic operations
#integers in python are whole numbers, they can be positive or negative, but they cannot have a decimal point. They are represented by the int data type.
2 + 3  #addition
5 - 2  #subtraction
4 * 3  #multiplication
10 / 2  #division 
10 // 3  #floor division
10 % 3  #modulus     

#floats in python are numbers that can have a decimal point, they can be positive or negative. They are represented by the float data type.
3.14 + 2.86  #pi + another float
5.0 - 2.5  #subtraction
4.5 * 3.2  #multiplication
10.0 / 2.0  #division
10.0 // 3.0  #floor division
10.0 % 3.0  #modulus


#integers and floats can be used in arithmetic operations, and the result will be a float if any of the operands is a float.
#example of arithmetic operations with integers and floats
1 + 2.0  #addition
3 - 1.5  #subtraction 
2 * 3.0  #multiplication
4 / 2.0  #division

#underscores can be used in numbers to make them more readable, they are ignored by python.
#example of using underscores in numbers
universe_age = 14_000_000_000  #14 billion years
print(universe_age)  #prints 14000000000

#multiple assignment is a way to assign values to multiple variables in a single line of code. It can be used to assign the same value to multiple variables or to assign different values to different variables.
#example of multiple assignment
x ,y ,z  = 1 ,3 ,2
a ,b ,c  = 0 ,0 ,0

#Constant variables are variables that are assigned a value that should not be changed throughout the program. In Python, there is no built-in way to create constant variables, but it is a convention to use uppercase letters for constant variable names.
#example of constant variable
MAX_CONNECTIONS = 45000  #maximum number of connections


#TRY IT YOURSELF 
    #addition of two numbers
num_1 = 3
num_2 = 5 
sum = num_1 + num_2 
print(f'the sum of {num_1} and {num_2} is {sum}')  #prints the sum of two numbers

    #subtraction of two numbers
num_1 = 14
num_2 = 6
difference = num_1 - num_2
print(f'the difference of {num_1} and {num_2} is {difference}')  #prints the difference of two numbers

    #multiplication of two numbers
num_1 = 4
num_2 = 2
product = num_1 * num_2
print(f'the product of {num_1} and {num_2} is {product}')  #prints the product of two numbers

    #division of two numbers
num_1 = 32
num_2 = 4
quotient = num_1 / num_2
print(f'the quotient of {num_1} and {num_2} is {quotient}')  #prints the quotient of two numbers

#comments are used to explain the code and make it more readable. They are ignored by the python interpreter and do not affect the execution of the code. Comments can be single-line or multi-line. Single-line comments start with a hash symbol (#) and continue until the end of the line. Multi-line comments are enclosed in triple quotes (''' or """) and can span multiple lines. 
