print('List')

# create new list
arr = [1,3,2,4,5,7,8]

# access list values
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr[5])
print(arr[6])

# update list
arr[0] = 20
# arr[0] = '20'
# arr[0] = True
print(arr)

# get length of list
arr1 = 'strings '

print( len(arr) )
print( len(arr1) )

# insert new record in list
arr.append(10)
# arr.append('10')
print( arr )

# insert multiple values in list
# arr.append( [10,20,30,40] )
arr.extend([10,20,30,40])
print( arr )

# append element at given/specific index
# arr.insert(0,100)
arr.insert(5,100)
print( arr )

# remove any value from list
# arr.remove(100)
arr.remove(10)
print( arr )

# remove last value from list
# arr.pop()
poped_element = arr.pop()
print(poped_element)
print(arr)

# 2
poped_element1 = arr.pop(4)
print(poped_element1)
print(arr)

# get index of any value in list
index = arr.index(100)
# index = arr.index(20)
print(index)

# count the elements
a = arr1.count('s')
b = arr.count(3)
print(b)

# sort the list
# ascending form lowest to highest
# arr.sort(reverse=False)
arr.sort()

# print(arr)

# descending highest to lowest
# arr.sort(reverse=True)
# print(arr)

# revese order the list
arr.reverse()
print(arr)

# create copy of the list

copy = arr.copy()
print(copy)

# empty the entire list
# arr.clear()
# print(arr)


# check if value present in list
if( 12 in arr ):
    print('found')
else:
    print('not found')


# check types of variables/ list

print( type(arr1) )
print( type(arr) )

# 2
print( isinstance(arr1,str) )
print( isinstance(arr,list) )

# 3
arr = 120
# print(arr[0])

if( type(arr) is list):
    print( f'list 1st value is: {arr[0]}')
else:
    print(arr)




















