#Player starts in tile 1,1. 
#Travel directions pop up whenever player enters a new square (the ways he can go.)
#Input should be (N)orth (up), (E)ast (right), (S)outh (up), (W)est (left).
#"Invalid directions" is printed when user inputs an invalid directions.
#Instructions to winning the maze: (3x3 tiles) 1,1 -- > 1,2 ; 1,2 --> 1,3 or 2,2 or 1,1 ; 1,3 --> 2,3 or 2,2; 2,3 --> 3,3; 3,3 --> 3,2; 3,2 --> 3,1 (Victory tile).
#User can always backtrack, unless he has gotten to the victory tile. 



def movement(user_input):
    if user_input == "n":
        y = 1
        return y
    elif user_input == "s":
        y = - 1
        return y
    elif user_input == "w":
        x = - 1
        return x
    elif user_input  == "e":
        x = + 1
        return x 

def first_colum_instructions(x, y):
    if x == 1 and y == 1:
        directions = "(N)orth"
    elif x == 1 and y == 2:
        directions = "(N)orth or (E)ast or (S)outh"
    elif x == 1 and y == 3:
        directions = "(E)ast or (S)outh"
    return directions




    

x, y = 1, 1
    
while (x != 3 and y != 1) and (x < 4 and y < 4) :
    print("You can travel:", first_colum_instructions(x, y))
    user_input = input("Direction: ").lower()
    the_movement = movement(user_input)
    if user_input == "w" or user_input == "e":
        x += the_movement
    elif user_input == "n" or user_input == "s":
        y += the_movement
    else:
        print("Not a valid direction!")
    












    