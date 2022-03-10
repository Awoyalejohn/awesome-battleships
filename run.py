from random import randint, sample
score = {"Player": 0, "Computer": 0}
class Game:
    """ The game class that is reponsible for the objects that will be in the game"""
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
        return [["+"] * 5 for i in range(5)]


#code from code instute battleship demo
class Computer(Game):
    """
    Computer Grid class that holds information on the player,
    their side and ships
    """
    pass

#code from code instute battleship demo
class Player(Game):
    """
    Player Grid class that holds information on the player,
    their side and ships
    """
    pass

#computer ship index locations
computer_ship_row = sample(range(5), 4)
computer_ship_col = sample(range(5), 4)
print(computer_ship_row)
print(computer_ship_col)

def computer_ship_placement():
    """ places ships on the computer's grid using the first
    4 numbers from random number list"""
    hidden_grid[computer_ship_row[0]][computer_ship_col[0]] = "$"
    hidden_grid[computer_ship_row[1]][computer_ship_col[1]] = "$"
    hidden_grid[computer_ship_row[2]][computer_ship_col[2]] = "$"
    hidden_grid[computer_ship_row[3]][computer_ship_col[3]] = "$"



#player ship index locations 
player_ship_row = sample(range(5), 4)
player_ship_col = sample(range(5), 4)
print(player_ship_row)
print(player_ship_col)

def computer_ship_placement():
    """ places ships on the player's grid using the first
    4 numbers from random number list"""
    player_grid[player_ship_row[0]][player_ship_col[0]] = "$"
    player_grid[player_ship_row[1]][player_ship_col[1]] = "$"
    player_grid[player_ship_row[2]][player_ship_col[2]] = "$"
    player_grid[player_ship_row[3]][player_ship_col[3]] = "$"







def display_grid(grid):
    for i in grid:
        print(" ".join(i))

print(Game.info)
print(score)
hidden_grid = Game([])
player_grid = Player([])
computer_grid = Computer([])
hidden_grid = hidden_grid.create_grid()
player_grid = player_grid.create_grid()
computer_grid = computer_grid.create_grid()
print("Hidden Grid")
display_grid(hidden_grid)
print("Computer Grid")
display_grid(computer_grid)
print("Player Grid")
display_grid(player_grid)

