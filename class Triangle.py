class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    def Perimeter(self):
        return (self.a + self.b + self.c)
    

t1 = Triangle(3, 4, 5)
t2 = Triangle(7, 5, 9)

print(f'The perimeter of Triangle 1 is {t1.Perimeter()}')
print(f'The perimeter of Triangle 2 is {t2.Perimeter()}')