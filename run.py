import random


class PlayerGrid:
    """
    Player Grid class that holds information on the player,
    their side and ships
    """
    def __init__(self, player, player_side, player_ships):
        self.player = player
        self.player_side = player_side
        self.player_ships = player_ships

    def create_pgrid(self):
        """
        Creates a grid for the player
        """
        symbol = "o"
        for i in range(gsize):
            for j in range(gsize):
                print(symbol, end=" ")
            print()


class ComputerGrid:
    """
    Computer Grid class that holds information on the player,
    their side and ships
    """
    def __init__(self, computer, computer_side, computer_ships):
        self.computer = computer
        self.computer_side = computer_side
        self.computer_ships = computer_ships

    def create_cgrid(self):
        """
        Creates a grid for the computer
        """
        symbol = "o"
        for i in range(gsize):
            for j in range(gsize):
                print(symbol, end=" ")
            print()


def welcome():
    """
    Function that prints a group of strings that will
    appear before anything else
    """
    print("Welcome to Awesome Battleships!")
    print("Player and Computer Board size: 5")
    print("Number of ships: 4")
    print("from the top left corner")
    print("Row: 0")
    print("Column: 0")


def grids_size():
    """
    Gets the user input for the grid size
    and validates it if its a number between 4 and 6
    """
    while True:
        x = input("What size grid? Needs to be between 4 and 6\n")
        try:
            if int(x) == 4 or int(x) == 5 or int(x) == 6:
                return int(x)
        except ValueError:
            print("Needs to be a number between 4 and 6")
        except Exception:
            print("Needs to be a number between 4 and 6")
        else:
            print("Needs to be a number between 4 and 6")


welcome()
gsize = grids_size()


pgrid = PlayerGrid("Player's Grid:", gsize, "player ships")
print(pgrid.player)
pgrid.create_pgrid()
print("-" * 20)
cgrid = ComputerGrid("Computer's Grid:", gsize, "player ships")
print(cgrid.computer)
cgrid.create_cgrid()
