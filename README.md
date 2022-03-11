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

- Random grid generation
  - Ships are placed randomly on the player and computer grids
  - Player's ships are denoted with a dollar sign ($)
  - Computer's ships are not visible to the player
