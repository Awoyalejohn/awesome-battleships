from random import randint, sample
score = {"Player": 0, "Computer": 0}


class Game:
    """ The game class that is reponsible for the objects
     that will be in the game. It be used to make grid class instances
     and is a superclass of the Computer and Player classes"""
    info = """
    Welcome to Awesome Battleships!
    Player and Computer Board size is up to you:
    Number of ships for on each grid: 4
    From the top left corner
    Row: 0
    Column: 0
    """

    def __init__(self, grid):
        """"Creates class instance attributes for grids"""
        self.grid = grid

    def create_grid(self):
        """ A method to make a 2d grid that is made up
         of 5 lists made up of 5 plusses in a list """
        return [["+"] * size for i in range(size)]


# Code from code instute battleship demo
class Computer(Game):
    """
    Computer class that is a subclass of the Game class.
    It will be used to make class instances for the computer grid
    """
    pass


# Code from code instute battleship demo
class Player(Game):
    """
    Player class that is a subclass of the Game class.
    It will be used to make class instances for the player grid
    """
    pass


print(Game.info)

while True:
    try:
        size = int(input("Enter a grid size between 4 & 10: "))
        if size not in range(4, 11):
            raise ValueError
        break
    except ValueError:
        print("Must be a number between 4 & 10")

# Computer ship index locations
# Creates a random list of numbers with no repeats
computer_ship_row = sample(range(size), 4)
computer_ship_col = sample(range(size), 4)


def computer_ship_placement():
    """ places ships on the computer's grid using the first
    4 numbers from random number list"""
    hidden_grid[computer_ship_row[0]][computer_ship_col[0]] = "$"
    hidden_grid[computer_ship_row[1]][computer_ship_col[1]] = "$"
    hidden_grid[computer_ship_row[2]][computer_ship_col[2]] = "$"
    hidden_grid[computer_ship_row[3]][computer_ship_col[3]] = "$"


# Player ship index locations
# Creates a random list of numbers with no repeats
player_ship_row = sample(range(size), 4)
player_ship_col = sample(range(size), 4)


def player_ship_placement():
    """ places ships on the player's grid using the first
    4 numbers from random number lists"""
    player_grid[player_ship_row[0]][player_ship_col[0]] = "$"
    player_grid[player_ship_row[1]][player_ship_col[1]] = "$"
    player_grid[player_ship_row[2]][player_ship_col[2]] = "$"
    player_grid[player_ship_row[3]][player_ship_col[3]] = "$"


def player_guess_hit():
    """places an "o" on the computer grid if the player guesses right
    and increments the player's score by 1"""
    print(f"Player targets {guess_row}, {guess_col}")
    print("Player's attack hits")
    computer_grid[guess_row][guess_col] = "o"
    score["Player"] += 1


def player_guess_miss():
    """places an "x" on the computer grid if the player guesses wrong"""
    print(f"Player targets {guess_row}, {guess_col}")
    print("Player misses!")
    computer_grid[guess_row][guess_col] = "x"


def computer_guess_randomiser():
    """Creates a random tuple of a row and columnn within
    the range of grid size minus 1. It checks to see if
    the row and col index does not already have an "o" placed
    on player grid if it does it continues to loop the randint function"""
    while True:
        row = randint(0, len(hidden_grid) - 1)
        col = randint(0, len(hidden_grid) - 1)
        if (player_grid[row][col] == "o") or (player_grid[row][col] == "x"):
            continue
        else:
            return (row, col)


def computer_guess_hit():
    """ Adds an "o" to a location on the player's grid
    that the computer guessed rightand increments the
    computer's score by 1"""
    print(f"Computer targets {comp_guess[0]}, {comp_guess[1]}")
    print("Computer's attack hits!")
    player_grid[comp_guess[0]][comp_guess[1]] = "o"
    score["Computer"] += 1


def computer_guess_miss():
    """ Adds an "x" to a location on the player's grid
    that the computer guessed wrong"""
    print(f"Computer targets {comp_guess[0]}, {comp_guess[1]}")
    print("Computer misses!")
    player_grid[comp_guess[0]][comp_guess[1]] = "x"


def display_grid(grid):
    """Takes the grid lists as a parameter and returns
    them as a string separated by a space without
    square brackets or quotation marks"""
    for i in grid:
        print(" ".join(i))

print(score)
hidden_grid = Game([])
player_grid = Player([])
computer_grid = Computer([])
hidden_grid = hidden_grid.create_grid()
player_grid = player_grid.create_grid()
computer_grid = computer_grid.create_grid()

computer_ship_placement()
player_ship_placement()


def display_all_grids():
    """ Displays all the grids"""
    print("Computer Grid")
    display_grid(computer_grid)
    print("Player Grid")
    display_grid(player_grid)

display_all_grids()

# Main game Loop!
while (score["Player"] < 4) and (score["Computer"] < 4):
    try:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Column: "))
    except ValueError:
        print("Please type in a whole number!")
        continue

    try:
        if ((hidden_grid[guess_row][guess_col] == "$") and
                (not computer_grid[guess_row][guess_col] == "o")):
            player_guess_hit()
        else:
            if ((guess_row not in range(size)) or
                    (guess_col not in range(size))):
                print("You can't use negative numbers!")
                continue

            elif (computer_grid[guess_row][guess_col] == "x"):
                print("You guessed that one wrong already!")
                continue

            elif (computer_grid[guess_row][guess_col] == "o"):
                print("You guessed that one correct already!")
                continue
            else:
                player_guess_miss()
    except IndexError:
        print("Your guess is off-grid")
        continue

    comp_guess = computer_guess_randomiser()

    if (player_grid[comp_guess[0]][comp_guess[1]] == "$"):
        computer_guess_hit()

    else:
        computer_guess_miss()
    print(score)
    display_all_grids()

if score["Player"] == score["Computer"]:
    print("Game Over, It's a draw!")
elif score["Player"] > score["Computer"]:
    print("Game over, you win!")
else:
    print("Game over, you lose!")
