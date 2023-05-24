import os
from argparse import ArgumentParser
from circle_of_life import CircleOfLife

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--timesteps', type=int, default=10)
    parser.add_argument('--worldsize', type=int, default=5)
    parser.add_argument('--num_zebras', type=int, default=5)
    parser.add_argument('--num_lions', type=int, default=2)
    args = parser.parse_args()
    print(args)
    input('press enter to start')

    safari = CircleOfLife(args.worldsize, args.num_zebras, args.num_lions)
    safari.run(args.timesteps)