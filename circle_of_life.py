from animal import Zebra, Lion
import random
from utils import print_TODO

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        self.zebras = [Zebra(0, 0) for _ in range(num_zebras)]
        self.lions = [Lion(0, 0) for _ in range(num_lions)]
        self.update_grid()
        self.timestep = 0
        print_TODO('get random empty coordinates')
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')
    
    def update_grid(self):
        self.grid = [['.' for _ in range(self.world_size)]
                          for _ in range(self.world_size)]
        for animal in self.zebras:
            self.grid[animal.y][animal.x] = 'Z'
        for animal in self.lions:
            self.grid[animal.y][animal.x] = 'L'

    def display(self):
        print(f'Clock: {self.timestep}')
        top_coord_str = ' '.join([f'{coord + 1:3}' for coord in range(len(self.grid))])
        print('   ' + top_coord_str)
        for row, line in enumerate(self.grid):
            print(f'{ row + 1:3} ' + ' '.join(f'{cell:3}' for cell in line))
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        print_TODO('step_move()')
        for zebra in self.zebras:
            zebra.move(self.grid)
            self.update_grid()
        for lion in self.lions:
            lion.move(self.grid)
            self.update_grid
    
    def step_breed(self):
        print_TODO('step_breed()')

    
    def run(self, num_timesteps=100):
        self.display()
        for _ in range(num_timesteps):
            self.timestep +=1
            self.step_move()
            self.display()

            self.step_breed()
            self.display()

if __name__ == '__main__':
    safari = CircleOfLife(20, 5, 2)
    safari.run(10)