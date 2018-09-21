#Player starts in tile 1,1. 
#Travel directions pop up whenever player enters a new square (the ways he can go.)
#Input should be (N)orth (up), (E)ast (right), (S)outh (up), (W)est (left).
#"Invalid direction" is printed when user inputs an direction that is not allowed or invalid.
#Instructions to winning the maze: (3x3 tiles) 1,1 -- > 1,2 ; 1,2 --> 1,3 or 2,2 or 1,1 ; 1,3 --> 2,3 or 2,2; 2,3 --> 3,3; 3,3 --> 3,2; 3,2 --> 3,1 (Victory tile).
#User can always backtrack, unless he has gotten to the victory tile. 
#Github-id: https://github.com/Halldorv18/tile_traveller

x, y = 1, 1
victory = False
options = "ESWN"

print("You can travel: (N)orth.")
while victory == False:
    chose = input("Direction: ")
    chose = chose.upper()

    if chose in options:
    
        if chose == "E":
            x -=1
        elif chose == "S":
            y -=1
        elif chose == "W":
            x +=1
        elif chose == "N":
            y +=1
    else:
        print("Not a valid direction!")
        continue

    if x == 3 and y == 1:
            victory = True
            print("Victory!")
            break
    else:
           
        if x == 1 and y == 1:
            options = "N"
            string = "(N)orth."
        elif x == 1 and y == 2:
            options = "NES"
            string= "(N)orth or (E)ast or (S)outh."
        elif x == 1 and y == 3:
            options = "ES"
            string = "(E)ast or (S)outh."
        elif x == 2 and y == 1:
            options = "N"
            string = "(N)orth."
        elif x == 2 and y == 2:
            options = "SW"
            string = "(S)outh or (W)est."
        elif x == 2 and y == 3:
            options = "EW"
            string = "(E)ast or (W)est."
        elif x == 3 and y == 2:
            options = "NS"
            string = "(N)orth or (S)outh."
        elif x == 3 and y == 3:
            options = "SW"
            string = "(S)outh or (W)est."
        print("You can travel:", string)