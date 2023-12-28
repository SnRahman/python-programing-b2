class Vehicle:

    def __init__(self,brand,model,color,price):
        # public access all over 
        self.model = model
        self.brand = brand
        self.color = color
        self.price = price
        
        # private accesed over same class and inherited/ child class
        # self._parent_prv_var = 'parent'

        # can only be accessed in same class in which defined 
        # self.__parent_pro_var = 'Protected'

    def display(self):
        print(f' Brand : {self.brand} --  Modal:{self.model} -- color: {self.color} -- Price: {self.price} ')



# class Toyota(Vehicle):
#     # constructor
#     def __init__(self, modal, color, price):
#         super().__init__('Toyota',modal,color,price)
#         self._private_var = 'test'

#     def display_price(self):
#         # print(f"Price is : {self.price} -- Private: {self._private_var} --- parent : {self._parent_prv_var}  --- Protected: {self.__parent_pro_var}")
#         print(f"Price is : {self.price} -- Private: {self._private_var} --- parent : {self._parent_prv_var}")






# v = Vehicle('Toyota','Corolla','White','6m')
# v.display()

# v1 = Vehicle('Honda','Civic','Black','8m')
# v1.display()

# clid class object

# t= Toyota('Corolla','White','6m')
# # t.display()
# t.display_price()
# # print( t._parent_prv_var )

