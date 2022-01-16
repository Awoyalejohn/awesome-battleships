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

class ComputerGrid:
    """
    Computer Grid class that holds information on the player,
    their side and ships
    """
    def __init__(self, computer, computer_side, computer_ships ):
        self.computer = computer
        self.computer_side = computer_side
        self.computer_ships = computer_ships




print("Welcome to Awesome Battleships!")
print("Player and Computer Board size: 5")
print("Number of ships: 4")
print("from the top left corner")
print("Row: 0")
print("Column: 0")