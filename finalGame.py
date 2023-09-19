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
RABBIT_WITH_CARROT = 'R'
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

    # random rabbit position
    rabbit_x, rabbit_y = generate_random_coordinates()
    map[rabbit_x][rabbit_y] = RABBIT
    used_coordinates.add((rabbit_x, rabbit_y))

    # placing random carrots
    for _ in range(num_carrots):
        while True:
            carrot_x, carrot_y = generate_random_coordinates()
            if (carrot_x, carrot_y) not in used_coordinates:
                map[carrot_x][carrot_y] = CARROT
                used_coordinates.add((carrot_x, carrot_y))
                break

    # placing random rabbit holes
    for _ in range(num_rabbit_holes):
        while True:
            hole_x, hole_y = generate_random_coordinates()
            if (hole_x, hole_y) not in used_coordinates:
                map[hole_x][hole_y] = RABBIT_HOLE
                used_coordinates.add((hole_x, hole_y))
                break

    return map

# displaying the grid/map generated
def display_grid(map):
    for row in map:
        print(' '.join(row))


# Verify if the movement is within the restrictions
def is_valid_move(game_map, x, y, map_size):
    if 0 <= x < map_size and 0 <= y < map_size and game_map[x][y] != CARROT and game_map[x][y] != RABBIT_HOLE:
        return True
    return False


def pick_carrot(game_map, x, y, counter, map_size):
    if 0 < x < map_size-1 and 0 < y < map_size-1:
        if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y+1] == RABBIT_HOLE or game_map[x][y-1] == RABBIT_HOLE or game_map[x+1][y] == RABBIT_HOLE or game_map[x-1][y] == RABBIT_HOLE):
            game_map[x][y] = PATHWAY_STONE
            return counter+1
        else:
            if game_map[x][y+1] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x][y+1] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x][y-1] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x][y-1] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x+1][y] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x+1][y] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x-1][y] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x-1][y] = RABBIT_WITH_CARROT
                return counter+1
    elif x == 0 and y == 0:
        if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y+1] == RABBIT_HOLE or game_map[x+1][y] == RABBIT_HOLE):
            game_map[x][y] = PATHWAY_STONE
            return counter+1
        else:
            if game_map[x][y+1] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x][y+1] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x+1][y] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x+1][y] = RABBIT_WITH_CARROT
                return counter+1
    elif x == map_size-1 and y == map_size-1:
        if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y-1] == RABBIT_HOLE or game_map[x-1][y] == RABBIT_HOLE):
            game_map[x][y] = PATHWAY_STONE
            return counter+1
        else:
            if game_map[x][y-1] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x][y-1] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x-1][y] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x-1][y] = RABBIT_WITH_CARROT
                return counter+1
    elif x == 0 and y == map_size-1:
        if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y-1] == RABBIT_HOLE or game_map[x+1][y] == RABBIT_HOLE):
            game_map[x][y] = PATHWAY_STONE
            return counter+1
        else:
            if game_map[x][y-1] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x][y-1] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x+1][y] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x+1][y] = RABBIT_WITH_CARROT
                return counter+1
    elif x == map_size-1 and y == 0:
        if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y+1] == RABBIT_HOLE or game_map[x-1][y] == RABBIT_HOLE):
            game_map[x][y] = PATHWAY_STONE
            return counter+1
        else:
            if game_map[x][y+1] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x][y+1] = RABBIT_WITH_CARROT
                return counter+1
            elif game_map[x-1][y] == CARROT and game_map[x][y] == RABBIT:
                game_map[x][y] = PATHWAY_STONE
                game_map[x-1][y] = RABBIT_WITH_CARROT
                return counter+1
    else:
        if x == 0:
            if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y+1] == RABBIT_HOLE or game_map[x][y-1] == RABBIT_HOLE or game_map[x+1][y] == RABBIT_HOLE):
                game_map[x][y] = PATHWAY_STONE
                return counter+1
            else:
                if game_map[x][y+1] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x][y+1] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x][y-1] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x][y-1] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x+1][y] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x+1][y] = RABBIT_WITH_CARROT
                    return counter+1
        elif y == 0:
            if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y+1] == RABBIT_HOLE or game_map[x+1][y] == RABBIT_HOLE or game_map[x-1][y] == RABBIT_HOLE):
                game_map[x][y] = PATHWAY_STONE
                return counter+1
            else:
                if game_map[x][y+1] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x][y+1] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x+1][y] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x+1][y] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x-1][y] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x-1][y] = RABBIT_WITH_CARROT
                    return counter+1
        elif x == map_size-1:
            if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y+1] == RABBIT_HOLE or game_map[x][y-1] == RABBIT_HOLE or game_map[x-1][y] == RABBIT_HOLE):
                game_map[x][y] = PATHWAY_STONE
                return counter+1
            else:
                if game_map[x][y+1] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x][y+1] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x][y-1] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x][y-1] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x-1][y] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x-1][y] = RABBIT_WITH_CARROT
                    return counter+1
        elif y == map_size-1:
            if game_map[x][y] == RABBIT_WITH_CARROT and (game_map[x][y-1] == RABBIT_HOLE or game_map[x+1][y] == RABBIT_HOLE or game_map[x-1][y] == RABBIT_HOLE):
                game_map[x][y] = PATHWAY_STONE
                return counter+1
            else:
                if game_map[x][y-1] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x][y-1] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x+1][y] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x+1][y] = RABBIT_WITH_CARROT
                    return counter+1
                elif game_map[x-1][y] == CARROT and game_map[x][y] == RABBIT:
                    game_map[x][y] = PATHWAY_STONE
                    game_map[x-1][y] = RABBIT_WITH_CARROT
                    return counter+1



def rabbit_hole_jump(game_map, x, y, map_size):
    if 0 <= x < map_size and 0 <= y < map_size:
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < map_size and 0 <= new_y < map_size and game_map[new_x][new_y] == RABBIT_HOLE:
                current_rabbit = game_map[x][y]
                game_map[x][y] = PATHWAY_STONE
                game_map[new_x][new_y] = current_rabbit
                return


# Find the position of the rabbit on the map
def rabbit_position(map, map_size):
    for i in range(map_size):
        for j in range(map_size):
            if map[i][j] == RABBIT or map[i][j] == RABBIT_WITH_CARROT:
                return i, j


def move_rabbit(map,map_size,num_carrots,num_rabbit_holes):
    try:
        counter = 0
        while True:
            if counter==2:
                display_grid(map)
                print("-------------------------")
                print("Congratulations! You won!")
                print("-------------------------")
                break

            display_grid(map)
            rabbit_x, rabbit_y = rabbit_position(map, map_size)

            move = keyboard.read_event(suppress=True)
        
            if move.event_type == keyboard.KEY_DOWN:
                if move.name == 'q':
                    print("Exiting the game.")
                    break

            elif move.name == 'p' or move.name == 'j':
                os.system('cls')
                if move.name == 'p':
                    counter = pick_carrot(map, rabbit_x, rabbit_y, counter, map_size)
                elif move.name == 'j':
                    rabbit_hole_jump(map, rabbit_x, rabbit_y, map_size)
            else:
                new_x, new_y = rabbit_x, rabbit_y
                m = {'a', 'd', 'w', 's', 'wd', 'dw',
                    'wa', 'aw', 'as', 'sa', 'sd', 'ds'}
                if move.name in m:
                    if move.name == 'a':
                        new_y -= 1
                    elif move.name == 'd':
                        new_y += 1
                    elif move.name == 'w':
                        new_x -= 1
                    elif move.name == 's':
                        new_x += 1
                    elif move.name == 'wd' or move.name == 'dw':
                        new_x -= 1
                        new_y += 1
                    elif move.name == 'wa' or move.name == 'aw':
                        new_x -= 1
                        new_y -= 1
                    elif move.name == 'as' or move.name == 'sa':
                        new_x += 1
                        new_y -= 1
                    elif move.name == 'sd' or move.name == 'ds':
                        new_x += 1
                        new_y += 1

                    if is_valid_move(map, new_x, new_y, map_size):
                        current_rabbit = map[rabbit_x][rabbit_y]
                        map[rabbit_x][rabbit_y] = PATHWAY_STONE
                        rabbit_x, rabbit_y = new_x, new_y
                        map[rabbit_x][rabbit_y] = current_rabbit
                        os.system('cls')
                    os.system('cls')
                else:
                    os.system('cls')
                    print("Invalid move. Try again.")
    except Exception as e:
        print("Wrong key's pressed, ", e)
        print("--------------------")
        print("Restart the game...!")
        print("--------------------")

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
        
        print("Controls:")
        print("a: Move left")
        print("w: Move up")
        print("s: Move down")
        print("d: Move right")
        print("Combination of the above keys will lead to diagonal movement")
        print("p: Pick/drop the carrot")
        print("j: Jump over the hole")
        print("q: Quit")
        # generate a random map
        map = generate_map(map_size, num_carrots, num_rabbit_holes)

        # moving the rabbit after the map is generated
        move_rabbit(map,map_size,num_carrots,num_rabbit_holes)

if __name__ == "__main__":
    os.system('cls')
    print('Innstructions:')
    print('Press Enter to play the game; Press any other key to Quit.')
    print('Repeat the same after every play.')
    key = input()
    if key == "":
        main()
