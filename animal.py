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
                           if neighbor[1] >= 0
                           and neighbor[1] < world_width
                           and neighbor[0] >= 0
                           and neighbor[0] < world_height
                           and str(grid[neighbor[0]][neighbor[1]]) == target]
        return neighbors_valid

    def move_to(self, grid, target) -> bool:
        neighbors = self.get_neighbors(grid, target)
        if len(neighbors) > 0:
            grid[self.y][self.x] = Empty(self.y, self.x)
            chosen_neighbor = random.choice(neighbors)
            self.y, self.x = chosen_neighbor
            grid[self.y][self.x].hp = 0 
            grid[self.y][self.x] = self
            return True
        else:
            return False

    def breed(self, grid):
        child = self.__class__(self.y, self.x)
        child.move_to(grid, target='.')
        grid[self.y][self.x] = self

class Empty(Animal):
    def __str__(self):
        return '.' 

class Zebra(Animal):
    def __str__(self):
        return 'Z'
    
    def move(self, grid):
        self.move_to(grid, target='.')

    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 3 == 0
        
class Lion(Animal):
    def __str__(self):
        return 'L'
    
    def move(self, grid):
        # buffer = f'{self.y} {self.x}'
        hunt_is_successful = self.move_to(grid, target='Z')
        if hunt_is_successful:
            self.hp = 3
            # buffer += f' -> (ate) {self.y} {self.x}'
        else:
            self.move_to(grid, target='.')
            self.hp -= 1
            # buffer += f' -> (empty) {self.y} {self.x}'
        # print(buffer)
    
    def is_ready_to_breed(self):
        return self.age != 0 and self.age % 8 == 0


if __name__ == "__main__":
    print("hi")
