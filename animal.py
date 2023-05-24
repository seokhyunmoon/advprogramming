import random
from utils import print_TODO

class Animal:
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.age = 0
        self.hp = 3
    
    def get_neighbors(self, grid, target):
        world_height = len(grid)
        world_width = len(grid[0])
        y, x = self.y, self.x
        neighbors = []
        neighbors.append([y - 1, x])
        neighbors.append([y + 1, x])
        neighbors.append([y, x - 1])
        neighbors.append([y, x + 1])
        neighbors_valid = [neighbor for neighbor in neighbors
                           if neighbor[0] >= 0
                           and neighbor[0] < world_width
                           and neighbor[1] >= 0
                           and neighbor[1] < world_height
                           and str(grid[neighbor[1]][neighbor[0]]) == target]
        return neighbors_valid

    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            grid[self.y][self.x] = Empty(self.y, self.x)
            chosen_neighbor = random.choice(neighbors)
            self.y, self.x = chosen_neighbor
            grid[self.y][self.x].hp = 0 #kill
            grid[self.y][self.x] = self
            return True
        else:
            return False

    def breed(self, grid):
        print_TODO("Not Implemented")

class Empty(Animal):
    def __str__(self):
        return '.' 

class Zebra(Animal):
    def __str__(self):
        return 'Z'
    
    def move(self, grid):
        self.move_to(grid, target='.')

    def breed(self, grid):
        print_TODO("Not Implemented")
        
class Lion(Animal):
    def __str__(self):
        return 'L'
    
    def move(self, grid):
        hunt_is_successful = self.move_to(grid, target='Z')
        if hunt_is_successful:
            self.hp = 3
        else:
            self.move_to(grid, target='.')
            self.hp -= 1
    
    def breed(self, grid):
        print_TODO("Not Implemented")
        child = self.__class__(self.y, self.x)
        child.move_to(grid, target='.')
        grid[self.y][self.x] = self


if __name__ == "__main__":
    print("hi")
