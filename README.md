# Project Title:
                   Martin-Machines-on-a-Gridded-Quest

# Description:
             This program simulates the movement of explorers on a plateau on Mars. The plateau is defined by its upper-right corner coordinates. Each explorer is provided with an initial position (x, y, direction) and a sequence of commands (L, R, M) that determine its movement. The program calculates the final position and direction of each explorer and outputs the results.


Input Format
The input follows a specific format:  Explorer Class:
    In this project I have implement the class which consists of :    
   Explorer is a class that represents an explorer on a plateau. It has an __init__ method to initialize an explorer with an initial position (x, y) and direction (N, E, S, W).

It has methods turn_left, turn_right, and move to simulate turning left, turning right, and moving forward, respectively.

The first line specifies the plateau's size (upper-right corner coordinates).
Each subsequent pair of lines represents an explorer:

First line: Initial position (x, y, direction)
Second line: Sequence of "L", "R", and "M" commands.
              A string of L, R, and M commands:
              L: Turn left 90 degrees
              R: Turn right 90 degrees
              M: Move forward one unit

# Example Input:

5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

# Output
The program outputs the final position and direction of each explorer:
1 3 N
5 1 E

# Dependencies:
                The program requires Python 3.
