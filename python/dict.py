print('Dictionary')
arr = ['ahmad','ali','python',25,'ahmadali@gmail.com','030012345678']
print(arr)


# inilialize any dictionary
obj_dic = {
    'first_name': 'Ahmad',
    'last_name' : 'ali',
    'course' : 'python',
    'age' : 25,
    'email' : 'ahmadali@gmail.com',
    'phone' : '030012345678'
}

# access the dictionary values/keys
print(obj_dic)
print( obj_dic['first_name'] )
print( obj_dic['last_name'] )
print( obj_dic['age'] )
print( obj_dic['course'] )
print( obj_dic['email'] )
print( obj_dic['phone'] )
# print( arr[0] )

# add new key in dict
obj_dic['address'] = 'lahore'
print(obj_dic)

# update any key
obj_dic['age'] = 22
print(obj_dic)

# delete any key
del obj_dic['last_name']
print(obj_dic)


# tuples
# tup = [12,36,45,689]

tup = (12,36,45,689)
a = 'ahmad','ali'

print( type(a))
print( type(tup))

print(a)
print(tup)
# tup[3] = 3.14
print(tup[1])
