# cse210-01

_Tic Tac Toe  
by Mike Lewis  
CSE-210 Section 8  
25-Apr-2022_

> Tic-Tac-Toe  
> Love is a game of tic-tac-toe,  
> Constantly waiting for the next x or o.  
    _- Lang Leav -_

## Overview
Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

## Rules
Tic-Tac-Toe is played according to the following rules.

1. The game is played on a grid that is three squares by three squares.
2. Player one uses x's. Player two uses o's.
3. Players take turns putting their marks in empty squares.
4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
5. If all nine squares are full and neither player has three in a row, the game ends in a draw.

## Interface
```
1|2|3
-+-+-
4|5|6
-+-+-
7|8|9

x's turn to choose a square (1-9): 2

1|x|3
-+-+-
4|5|6
-+-+-
7|8|9

o's turn to choose a square (1-9): 5

1|x|3
-+-+-
4|o|6
-+-+-
7|8|9

x's turn to choose a square (1-9): _

...

x|x|x
-+-+-
4|o|6
-+-+-
7|8|o

Good game. Thanks for playing!
> _
```

## Requirements

Your program must also meet the following requirements.

1. [x] The program must have a comment with assignment and author names. 
2. [x] The program must have at least one if/then block.
3. [x] The program must have at least one while loop.
4. [x] The program must have more than one function.
5. [x] The program must have a function called main.

## Suggestions

Make the game in any way you like. A few ideas are as follows.
- [x] Enhanced input validation with user-friendly messages.
- [x] Enhanced game over messages (x's, o's or draw).
- [ ] Enhanced board size (4x4, 5x5, 6x6 grid, or user selected!)
- [x] Enhanced game display (different colors for each player)
