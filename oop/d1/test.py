count = 0
count1 = 0

print(count)


def counter1():
    global count1
    count1 += 1
def counter():
    global count
    count += 1

counter()
counter()
counter()
counter()
counter()


counter1()
counter1()
counter1()

print(count)
print(count1)
