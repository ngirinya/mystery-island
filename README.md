# Mystery Island: The Lost Lighthouse

## About the Project

Mystery Island is a simple text-based adventure game I built using Python.

In this game, the player explores a mysterious island, collects useful items and tries to reach the Lost Lighthouse. The main goal is to find the items needed to light the lighthouse beacon and win the game.

I built this project to practise my Python programming skills and understand how to use variables, functions, loops, conditions, lists and modules.

## Project Structure

The project contains different Python files, and each file has its own responsibility.

- `main.py` - Starts and controls the game.
- `game.py` - Handles the game menu, locations and movement.
- `player.py` - Handles the player's name, energy and replay option.
- `inventory.py` - Handles collecting and displaying items.
- `tests/test_game.py` - Contains tests for the game functions.
- `README.md` - Explains the project.

## How to Run the Game

1. Make sure Python 3 is installed on your computer.
2. Open the project folder in your terminal.
3. Run this command:

```bash
python3 main.py
```

## Game Rules

- The player starts at the Beach with 5 energy.
- Moving from one location to another uses 1 energy.
- The player can collect a Rope in the Jungle.
- The player can collect a Lantern in the Cave.
- The Rope is needed to cross the Old Bridge.
- The Lantern is needed to light the Lighthouse beacon.
- The player loses when their energy reaches zero.
- The player wins by reaching the Lighthouse and lighting the beacon with the Lantern.
- The player can choose to play again after finishing a game.

## Locations

The game has five locations:

1. Beach
2. Jungle
3. Cave
4. Old Bridge
5. Lighthouse

## Features

- Player name input.
- A menu for choosing actions.
- Movement between locations.
- Energy management.
- Inventory management.
- Collection of useful items.
- Input validation.
- Winning and losing conditions.
- Option to play again.

## Tests

I used Python's `unittest` module to test some of the game functions.

To run the tests, use:

```bash
python3 -m unittest discover -s tests -v
```

## Known Limitations

- The game runs in the terminal and does not have a graphical interface.
- The player has only 5 energy points.
- The game has one main winning path.
- The game progress is not saved after quitting.

## What I Learned

While building this project, I practised:

- Creating and using variables.
- Writing functions.
- Using `if`, `elif` and `else` statements.
- Using `while` loops.
- Working with lists.
- Getting input from users.
- Returning values from functions.
- Importing functions from other Python files.
- Organising code into modules.
- Testing Python functions.
- Finding and fixing errors in my code.