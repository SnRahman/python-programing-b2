class math:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        print(f"Sum is : {result}")
    def mul(self):
        result = self.a * self.b
        print(f"Mul is : {result}")
    def div(self):
        result = self.a / self.b
        print(f"Div is : {result}")

m1 = math(10,30)
m1.add()
m1.mul()
m1.div()