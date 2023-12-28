from vehicle import Vehicle

class Honda(Vehicle):
    def __init__(self,model, color, price):
        super().__init__('Honda', model, color, price)

    def display_color(self):
        print(f'Color is: {self.color}')


# h = Honda('City','Red','4m')
# h.display_color()

# v1 = Vehicle('Honda','Civic','Black','8m')
# v1.display()