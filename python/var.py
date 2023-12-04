'''
Tasks
1- Find the area of a rectangle where the length is 5 and the width is 8.
2- Find the area of a triangle where the lengths of the three sides are 8, 9, and 10.
3- Find the area of a circle where the radius is 3.
4- Convert temperatures from Celsius to Fahrenheit and Fahrenheit to Celsius.

'''

print('hello world!')

# comments
# single line
# integer 

# multi lines
''' 
a = 21
b = 53

'''


# Data types
a = 25
b = 12.0
c = 'hello'
d = True
l = [1,2,3,4,5,6]


print( type(a))
print(a)
print( type(b))
print(b)
print( type(c))
print(c)
print( type(d))
print(d)
print( type(l))
print(l)
print(l[0])


# concatenation all values must be str (string)
print('value of is' + c )

# concatenation string using format function
# single variable
print('value of a is: {}'.format(a) )

new_str = 'value of a is: {}'.format(a)
print( new_str )

# multi variables
print( 'A is :{} - B is:{} - C is:{} - D is:{} '.format(a,b,c,d)  ) 

# concatination using f format
print( 'value of a is: {}'.format(a) )
print( f'value of a is: {a}' )
print( f'A is :{a} - B is:{b} - C is:{c} - D is:{d} ')

# % formating
print( 'value of a is: %s ' %(a) )
print( 'A is :%d  - B is: %d - C is:%s - D is:%s ' %(a,b,c,d))

# assignment operator =

z = 59
print(z)

# arthimetic operators +, -, *, /. % ,  

y = 10

print( z + y )
print( z - y )
print( z * y )
print( z / y )
print( z % y )
print( z ** 3 )
print( z // y )

count = 2
# count = count + 1
# count += 1
# count -= 1
# count *= 10
# count /= 10
# count %= 10
count **= 10

print(count)

# example
string = 'a'

string += 'a '
string += 'a '
string += 'a '
string += 'a '
string += 'a '
string += 'a'
string += 'a'
string += 'a'
string += 'a'
print(string)





