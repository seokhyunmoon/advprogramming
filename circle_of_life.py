from animal import Empty, Zebra, Lion
import random
from utils import print_TODO

class CircleOfLife:

    def __init__(self, world_size, num_zebras, num_lions):
        self.world_size = world_size
        random.seed(0)
        zebra_coords, lion_coords = self.get_random_coords(num_zebras, num_lions)
        # self.zebras = [Zebra(0, 0) for _ in range(zebra_coords)]
        # self.lions = [Lion(0, 0) for _ in range(lion_coords)]
        for y, x in zebra_coords:
            self.grid = Zebra(y,x)
        for y, x in lion_coords:
            self.grid = Lion(y,x)
        self.update_grid()
        self.timestep = 0
        print_TODO('get random empty coordinates')
        print('Welcome to AIE Safari!')
        print(f'\tworld size = {world_size}')
        print(f'\tnumber of zebras = {len(self.zebras)}')
        print(f'\tnumber of lions = {len(self.lions)}')
    
    def get_random_coords(self, num_zebras, num_lions):
        all_coords = [(x,y) for y in range(self.world_size)
                      for x in range(self.world_size)]
        zebra_coords = random.sample(all_coords, num_zebras)
        all_coords= list(set(all_coords) - set(zebra_coords))
        lion_coords = random.sample(all_coords, num_lions)
        return zebra_coords, lion_coords
    
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
        # for row, line in enumerate(self.grid):
        #     print(f'{ row + 1:3} ' + ' '.join(f'{cell:3}' for cell in line))
        for row, line in enumerate(self.grid):
            buffer = [str(animal) for animal in line]
            print(f'{row:2} ' + ' '.join(buffer))
        key = input('enter [q] to quit:')
        if key == 'q':
            exit()

    def step_move(self):
        print_TODO('step_move()')
        # for zebra in self.zebras:
        #     zebra.move(self.grid)
        #     self.update_grid()
        # for lion in self.lions:
        #     lion.move(self.grid)
        #     self.update_grid
        animals = [animal in animals for line in self.grid for animal in line
                   if not isinstance(animal, Empty)]
        for animal in animals:
            if animal.hp != 0:
                animal.move(self.grid)
    
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