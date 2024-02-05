# This class represents an explorer on a plateau.
class Explorer:
    def __init__(self, x, y, direction):
    # Initializes an explorer with the given initial position and direction.

        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        #Turns the explorer 90 degrees to the left.
        directions = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.direction = directions[self.direction]

    def turn_right(self):
        #Turns the explorer 90 degrees to the right.
        directions = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = directions[self.direction]

    def move(self):
        #Moves the explorer one unit forward in the current direction.
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

def process_input(input_lines):
    #This function processes the input lines to extract relevant information.
    plateau_size = tuple(map(int, input_lines[0].split()))
#map():- returns an iterator, typically a map object, which can be converted to a list or
    # another iterable type using list() or tuple().
    explorers_data = input_lines[1:]
#This line creates a new list explorers_data by slicing input_lines starting from index 1.

    explorers = []
    for i in range(0, len(explorers_data), 2):
        position = tuple(map(int, explorers_data[i].split()[:2]))
        direction = explorers_data[i].split()[2]
        commands = explorers_data[i + 1].strip()

        explorers.append((position, direction, commands))

    return plateau_size, explorers

def Application():
    input_lines = [
        "5 5",
        "1 2 N",
        "LMLMLMLMM",
        "3 3 E",
        "MMRMMRMRRM"
    ]

    plateau_size, explorers_data = process_input(input_lines)
#This line calls the process_input function with input_lines as an argument.

    for position, direction, commands in explorers_data:
        expo = Explorer(*position, direction)
        for command in commands:
            if command == 'L':
                expo.turn_left()
            elif command == 'R':
                expo.turn_right()
            elif command == 'M':
                expo.move()

        print(f"{expo.x} {expo.y} {expo.direction}")

Application()

