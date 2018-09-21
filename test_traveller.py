#Player starts in tile 1,1. 
#Travel directions pop up whenever player enters a new square (the ways he can go.)
#Input should be (N)orth (up), (E)ast (right), (S)outh (up), (W)est (left).
#"Invalid direction" is printed when user inputs an direction that is not allowed or invalid.
#Instructions to winning the maze: (3x3 tiles) 1,1 -- > 1,2 ; 1,2 --> 1,3 or 2,2 or 1,1 ; 1,3 --> 2,3 or 2,2; 2,3 --> 3,3; 3,3 --> 3,2; 3,2 --> 3,1 (Victory tile).
#User can always backtrack, unless he has gotten to the victory tile. 
#Github-id: https://github.com/Halldorv18/tile_traveller

x, y = 1, 1