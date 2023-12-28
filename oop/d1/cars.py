class car:
    def __init__(self,color,model,brand):
        self._color = color
        self._model = model
        self._brand = brand

    def display_color(self):
        print(f"Color is :{self._color}")

    def display_model(self):
        print(f"Model is :{self._model}")
    
    def display_brand(self):
        print(f"Brand is :{self._brand}")
    def display_all(self):
        print(f'color: {self._color}')
        print(f'model: {self._model}')
        print(f'brand: {self._brand}')

class Honda(car):
    def __init__(self,color,model,brand):
        car.__init__(self,color,model,brand,"Honda")
    def display(self):
        print(f'color:{self.color}')
        print(f'model:{self.model}')
        print(f'brand:{self.brand}')

c1 = car ('black','civic','honda')
c1.display_all()