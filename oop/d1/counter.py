class counter:

    # constructor of any class 
    def __init__(self):
        self.count = 0
    # count = 0

    def inc_counter(self): 
        self.count += 1

    def display_current_counter(self):
        print( f"The current value of the counter is {self.count}")

# first object
c1 = counter()
c1.display_current_counter()
c1.inc_counter()

c1.display_current_counter()


# 2nd object
print('Object 2')
c2 = counter()
c2.display_current_counter()
c2.inc_counter()

c2.display_current_counter()

c1.inc_counter()
c1.display_current_counter()