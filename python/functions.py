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