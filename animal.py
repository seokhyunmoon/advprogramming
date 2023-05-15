import random
from utils import print_TODO

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.age = 0
    
    def get_neighbors(self, grid, target):
        world_height = len(grid)
        world_width = len(grid[0])
        x, y = self.x, self.y
        neighbors = []
        neighbors.append =([x-1, y])
        neighbors.append =([x+1, y])
        neighbors.append =([x, y-1])
        neighbors.append =([x, y+1])
        neighbors_valid = [neighbor for neighbor in neighbors
                           if grid[neighbor[1][neighbor[0]]] == target
                           and neighbor[0] >= 0
                           and neighbor[0] < world_width
                           and neighbor[0] >= 0
                           and neighbor[0] < world_height]
        return neighbors_valid


    def move(self, direction = "right"):
        print(f'moving to {direction}.')
        self.x += 1

    def breed(self, x, y):
        return Animal(x, y)
    
class Zebra(Animal):

    def move(self, grid):
        print(f'before: {self.x=}, {self.y=}')
        neightbors = self.get_neighbors(grid, target='.')
        if len(neightbors) > 0:
            chosen_neighbor = random.choice(neightbors)
            self.x, self.y = chosen_neighbor
        print(f'after: {self.x=}, {self.y=}')

    def breed(self, x, y):
        print()

class Lion(Animal):
    def move(self, grid):
        neighbors = self.get_neighbors(grid, target='Z')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(target='Z')
            if len(neighbors) > 0:
                chosen_neighbor = random.choice(neighbors)
                self.x, self.y = chosen_neighbor
                self.hp = 3
                return
        
        neighbors = self.get_neighbors(grid, target='.')
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            self.x, self.y = chosen_neighbor


    
    def breed(self,x, y):
        print("NOT IMPLEMENTED")
    
    def starve(self):
        print("NOT IMPLEMENTED")

if __name__ == "__main__":
    print("hi")
