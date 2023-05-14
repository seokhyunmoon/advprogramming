class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0

    def move(self, direction = "right"):
        print(f'moving to {direction}.')
        self.x += 1

    def breed(self, x, y):
        return Animal(x, y)
    
class Zebra(Animal):

    def move(self, occupancy_grid):
        print('<<< NOT IMPLEMENTED >>>')

    def breed(self, x, y):
        if self.age == 3:
            Zebra()
        else:
            pass

class Lion(Animal):
    def move(self, occupancy_grid):
        print("NOT IMPLEMENTED")
    
    def breed(self,x, y):
        print("NOT IMPLEMENTED")
    
    def starve(self):
        print("NOT IMPLEMENTED")

if __name__ == "__main__":
    print("hi")
