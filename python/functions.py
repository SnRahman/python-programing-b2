# Task
#     Check two given numbers and return true if one of the numbers is 50 or if their sum is 50.
#     Check from the given integer, whether it is positive or negative.
#     Check whether a given number is even or odd.
#     Check whether a given positive number is a multiple of 3.
#     check from the given two numbers, weather the first number is "greater", "lesser" or "equal" to the second number.
#     check from the three sides of triangle. use conditions to determine and display 
#     weather the triangle is "Equilateral" (all sides are equal), "Isosceles" (two sides are equal), or "Scalane" (no sides are equal)
#     check from the given month (1-12) if its "Winter" (December-Feburary), "Spring" (March-May), "Summer" (June-August), or "Autumn" OR "Fall" (September-November).
#     Create a function that takes two numbers as input and returns the largest of the two.
#     create a function that takes two strings as input and returns a new string that concatenates both if them.
#     Write a function that takes a temperature in celsius and converts it to Fahrenheit.
#     Write a program that takes the age and checks if they are eligible for voting (e.g 18 or older)
#     Implement a function that checks if a given number is positive, negative, or zero and return the result.
#     create a function that takes two numbers as input and returns their product  using arithmetic operations. (e.g the product of 2 and 3 is 6)
#     implement a function that takes two strings as input and checks if they are equal.
#     Write a function that takes a number as input and returns the absolute value of the number
#     Determine whether a given year is a leap year.
#     All the prior tasks are to be solved with functions.



print('functions')

# define function
def display():
    print('Hello functions')

# functions with parameters

def add(a,b):
    print(a+b)


# returning funtions
def sum(a,b):
    result = a+b
    return result
    # return a + b
    # print(a+b)

# call function
display()

a = sum(14,25)
print(a)
add(a,36)

# default parameters
def pow(base,power=2):
    a = base**power 
    print()

pow(10)
pow(10,3)
pow(10,4)

def mul(a,b,c,d):
    print(f'a is :{a}')
    print(f'b is :{b}')
    print(f'c is :{c}')
    print(f'd is :{d}')
    print(a*b*c*d)

# mul(1,2,3,4)
# mul(a=1,b=2,c=3,d=4)
mul(d=1,b=2,c=3,a=4)

# returning function example
def sub(a,b):
    # print(a-b)
    return a-b 


result = sub(10,5)
print(f'result is : {result}')