import random
class Game:
    """ The game class that is reponsible for the objects that will be in the game"""
    score = {"Player": 0, "Computer": 0}
    info = """Welcome to Awesome Battleships! 
    Player and Computer Board size: 
    5 Number of ships: 4
    from the top left corner
    Row: 0
    Column: 0
    """
    size = 5
    def __init__(self, grid):
        self.grid = grid

    def create_grid(self):
        self.grid = [["+"] * 5 for i in range(5)]


#code from code instute battleship demo
class Player(Game):
    """
    Player Grid class that holds information on the player,
    their side and ships
    """
    pass

#code from code instute battleship demo
class Computer(Game):
    """
    Computer Grid class that holds information on the player,
    their side and ships
    """
    pass



print(Game.info)
hidden_grid = Game([])
player_grid = Player([])
computer_grid = Computer([])
print(hidden_grid.create_grid())
print(player_grid.create_grid())
print(computer_grid.create_grid())
