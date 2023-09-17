import random
import keyboard
import os


# game elements
'''
Rabbit (denoted by the character “r” and “R”)
Carrot (denoted by the character “c”)
Rabbit hole (denoted by the character “O”)
Pathway stone (denoted by the character “-”)
'''
RABBIT = 'r'
BIG_RABBIT = 'R'
CARROT = 'c'
RABBIT_HOLE = 'O'
PATHWAY_STONE = '-'

# Random map generator
def generate_map(map_size, num_carrots, num_rabbit_holes):
    map = [[PATHWAY_STONE for _ in range(map_size)] for _ in range(map_size)]

    def generate_random_coordinates():
        x, y = random.randint(0, map_size - 1), random.randint(0, map_size - 1)
        return x, y

    used_coordinates = set()

    # Place rabbit
    rabbit_x, rabbit_y = generate_random_coordinates()
    map[rabbit_x][rabbit_y] = RABBIT
    used_coordinates.add((rabbit_x, rabbit_y))

    # Place carrots
    for _ in range(num_carrots):
        while True:
            carrot_x, carrot_y = generate_random_coordinates()
            if (carrot_x, carrot_y) not in used_coordinates:
                map[carrot_x][carrot_y] = CARROT
                used_coordinates.add((carrot_x, carrot_y))
                break

    # Place rabbit holes
    for _ in range(num_rabbit_holes):
        while True:
            hole_x, hole_y = generate_random_coordinates()
            if (hole_x, hole_y) not in used_coordinates:
                map[hole_x][hole_y] = RABBIT_HOLE
                used_coordinates.add((hole_x, hole_y))
                break

    return map

# display the grid/map generated
def display_grid(map):
    for row in map:
        print(' '.join(row))

def main():
        # Initialize game parameters using custom inputs

        # custom grid size
        map_size = int(input("Enter the size of the grid (minimum 10): "))
        while map_size < 10:
            map_size = int(input("Please enter grid size of atleast 10: "))
        # custom carrots
        num_carrots = int(input("Enter the number of carrots (grater than 1): "))
        while num_carrots <= 1:
            num_carrots = int(input("Please enter number of carrots greater than 1: "))
        # custom rabbit holes
        num_rabbit_holes = int(input("Enter the number of rabbit holes (grater than 1): "))
        while num_rabbit_holes <= 1:
            num_rabbit_holes = int(input("Please enter number of holes greater than 1: "))
        
        map = generate_map(map_size, num_carrots, num_rabbit_holes)
        display_grid(map)
        # move_rabbit(game_map,map_size,num_carrots,num_rabbit_holes)

if __name__ == "__main__":
    os.system('cls')
    print('Innstructions:')
    print('Press Enter to play the game; Press any other key to Quit.')
    print('Repeat the same after every play.')
    key = input()
    if key == "":
        main()