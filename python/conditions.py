print('conditions')
a = 20

# if condition
if(a==10):
    print('true')
    print(f'value is :{a}')
print('true1')


# if else
if(a==10):
    print('true')
    print(f'value is :{a}')
else:
    print('false')
    print(f'value is :{a}')

# if else if
if(a==10):
    print('true')
    print(f'value is :{a}')
elif(a==20):
    print('true')
    print('2nd condition')
    print(f'value is :{a}')
else:
    print('false')
    print(f'value is :{a}')

# comparison operators == != < > <= >=

# if(a != 10):
if(a is not 10):
    print('true')
    print('Not')
    print(f'value is :{a}')


# example
age = 65
if(age >= 18):
    print("allowed")
else:
    print("not allowed")


# gates And OR not

# and keyword
if(age >= 18 and age<=75):
    print("allowed")
else:
    print("not allowed")

# or keyword
month = 'dec'
if(month == 'dec' or  month=='jan' or month=='feb'):
    print('winter')






