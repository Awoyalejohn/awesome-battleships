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

    
    def create_grid(self):
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
    return int(input("What size grid"))


welcome()
gsize = grids_size()

pgrid = PlayerGrid("player", gsize, "player ships" )
pgrid.create_grid()