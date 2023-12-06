# Task
"""
1- Sum all the list elements by using both a loop and a Python built-in function.
2- Reverse the list by using both a loop and a Python built-in function.
3- Make a table of the given number with all possible loops.
4- Find the largest number in a list by using both a loop and a Python built-in function.
5- Find the smallest number in a list by using both a loop and a Python built-in function.
6- Add the list element at the specified index.
7- Delete the list element from the specified index.
8- Make a normal list to store the name of 5 students and iterate with for loop.
9- Make an associative list to store the name of 5 students and iterate with a for loop.
10- Make a normal list of associative Lists(a list that will have associative Lists) to store the information of 
    least 2 students and access them as hard-coded.
    Information to store:
        A- Name, age, registration number, course, favorite programming languages (should be a normal list), 
           Marks of 5 different subjects (should be an associative list).
    The operations to perform:
        B- Display every single value for any student.
        C- Display the first and last favorite programming languages of any student.
        D- Display the marks of any two subjects for any student.
"""


print('Hello Loops')
# print('Loops')
# print('Loops')
# print('Loops')
# print('Loops')
# print('Loops')
# print('Loops')
# print('Loops')
# print('Loops')
# print('Loops')


# for 
# give end limit or index in range
# for i in range(10):
#     print(f'{i} - Hello Loops!')

# give start and end index in range
# for i in range(1,11):
#     print(f'{i} - Hello Loops!')

# in third parameter define custome increment 
# for i in range(1,11,2):
#     print(f'{i} - Hello Loops!')

# revese loop, iteration
# for i in range(10,0,-2):
    # print(i)
    # print('Hello Loops!')
    # print(f'{i+1} - Hello Loops!')
    # print(f'{i} - Hello Loops!')


lis = ['Ahmad','Ali','Abdullah','Ahsan','Farrukh','Adnan','Adeel']
print(lis)
# print(lis[2])

# General for in loop
# for li in lis:
#     print(li)

# index and values 
# for index,value in enumerate(lis) :
#     print( f'{index} - {value} ')

obj_dic = {
    'first_name': 'Ahmad',
    'last_name' : 'ali',
    'course' : 'python',
    'age' : 25,
    'email' : 'ahmadali@gmail.com',
    'phone' : '030012345678'
}

print(obj_dic)
# print(obj_dic['first_name'])
# print(obj_dic['age'])

# for key in obj_dic:
    # print(f'{key} - {obj_dic[key]}')
    # print(key)
    # print(obj_dic[key])

# get both key and values from object
# for key,value in obj_dic.items() :
#     print(f'{key} - { value}')

'''
for i in lis:
    print(i)
    if i is 'Ahsan ali':
        # break the loop on given condition and future iterations will be cancelled
        break

#  else case runs when loop successfully completed without break or any other intruption
else:
    # print("This is the end of the loop")
    print("Value not found")
'''
# continue
# skip the current iteration and jumps to next iteration.

''' 
for i in lis:
    if i is 'Ahsan':
        print(f'{i} - mail blocked')
        continue
    print(f'{i} -  mail sended')
'''

# while loop runs untile condition is true
""" 
count = 1
check = True
# while count <=100:
while check is True:
    count += 1
    print(count)

    if count is 50:
        check = False
"""

# break with while on list
""" 
lis_length = len(lis)
print(f'list length : {lis_length}')
i = 0

while i < lis_length :
    value = lis[i]
    # print( f' {i} - { lis[i] }' )
    print( f' {i} - { value }' )

    if value is 'Ahsan':
        break

    i += 1
"""

# continue with while on list

lis_length = len(lis)
print(f'list length : {lis_length}')
i = 0

while i < lis_length :
    value = lis[i]
    # print( f' {i} - { lis[i] }' )
    print( f' {i} - { value }' )
    i += 1

    if value is 'Ahsan':
        print(f'{i} - mail blocked')
        continue
    
    print(f'{i} -  mail sent')






















# [start_index : end_index]
# for li in lis[2:]:
# for li in lis[2:5]:
#     print(li)
