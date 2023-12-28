from vehicle import Vehicle 
class Suzuki(Vehicle):

    def __init__(self, model, color, price):
        super().__init__('Suzuki', model, color, price)

    def display_model(self):
        print(f'Medel is : {self.model}')

# s = Suzuki('Mehran','white','8m')
# s.display_model()