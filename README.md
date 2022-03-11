# Awesome Battleships
Awesome Battleships is a python game that runs on a mock command line terminal on Heroku. It's a one-on-one game in which you compete against the computer.
You and the computer battle to sink each other's ships, which are distributed across a grid.
Each ship occupies a single point on the grid.

The live link can be found here - ...

add mockup image here*

## How To Play
The player will be prompted to enter a grid size for their own and the computer's grids when the game begins. They can only choose between 4 and 10. Then the player and computer's ships are placed on the grid, but only the player's ships are visible to them, while the computer's remain hidden. The player's ships are indicated with a dollar sign ($).
When they make a correct guess, it is indicated by an "o," and when they make a wrong guess, it is marked by a "x" on the computer's grid. The winner is the one who destroys all of the opponent's ships. It is possible for the game to end in a draw if all ships are cleared in the same round.

## Features

## Existing Features
- Grid size set
  - The grid size can be set at the start of the game
  - The choice is between 4 and 10
  - The player grid and computer grid will be sized the same
  - Warns player if their choice is not between 4 and 10
add image here*

- Random grid generation
  - Ships are placed randomly on the player and computer grids
  - Player's ships are denoted with a dollar sign ($)
  - Computer's ships are not visible to the player
add image here*

- turn based gameplay
  - Computer can makes guesses after player's guess
  - Score is revealed every turn
  - Player is prompted to give their guess on each turn
add image here*

- Input validation and error-checking
  - Player is unable to enter coordinates that are outside the grid size. 
  - Player can only input numbers for guesses
  - Player is unable to make the same gueess twice
add image here*

### Future Features
- Larger ships that can take up more points on the grid
- Option to change ship axis
- More ships for larger grids size options
- Special ships that reward more points when destroyed

## Testing
I tested that the game works through a variety of methods:
- I used the pep8 linter and confirmed there are no problems
- I inputed random letters when prompted for number inputs
- I input coordinates that were out of range
- I typed in negative numbers
- I also used duplicate guesses

### Bugs

### Solved bugs
- I had issues with my try exceptions not picking up on value error exceptions when I was testing the game. It turns out I had not indented my code correctly by having both spaces and tabs mixed in. I fixed it by deleting all the white space and only indendting with 4 spaces.

- I had originally used the random randint function to pick a random row and colums to place the ships on, but it would repeat iself sometimes and place ships in the same location. I fixed this by using the random sample funcion instead. Which creates a random list with no duplicates that I used to index the location of the ships to be placed.

## Validator Tesring
- PEP8
  - No errors were returned from [pep8online validator.](pep8online.com)

### Unfixed Bugs
No unfixed bugs

## Deployment
- This project was deploued on Heroku
  - Clone the repository
  - Create a new Heroku app
  - Set the buildbacks to python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on Deploy

The live link can be found here -...

### Credits
- The code used to add randoms numbers within [range.](https://www.programiz.com/python-programming/examples/random-number)

- The code used to add random numbers in a list with no duplicates using the random sample [function.](https://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-random-numbers-without-duplicates)

- Code used to return multiple values from a [function.](https://stackoverflow.com/questions/354883/best-way-to-return-multiple-values-from-a-function)

- Code and project used to help understand battleship game's [logic.](https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship)

- Code used make input validation [prompts.](https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers)




