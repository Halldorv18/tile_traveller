#Player starts in tile 1,1. 
#Travel directions pop up whenever player enters a new square (the ways he can go.)
#Input should be (N)orth (up), (E)ast (right), (S)outh (up), (W)est (left).
#"Invalid direction" is printed when user inputs an direction that is not allowed or invalid.
#Instructions to winning the maze: (3x3 tiles) 1,1 -- > 1,2 ; 1,2 --> 1,3 or 2,2 or 1,1 ; 1,3 --> 2,3 or 2,2; 2,3 --> 3,3; 3,3 --> 3,2; 3,2 --> 3,1 (Victory tile).
#User can always backtrack, unless he has gotten to the victory tile. 
#Github-id: https://github.com/Halldorv18/tile_traveller


def movement(user_input, x, y):
    move = 0
    if user_input == "n" and y != 3:
        move = 1
    elif user_input == "e" and x != 3:
        move =  1
    elif user_input == "s" and y != 1:
        move = -1 
    elif user_input == "w" and x != 1:    
        move = 1
    else:
        move = 0
    return move


def instructions(x, y):
    if x == 1 and y == 1:
        directions1 = "(N)orth."
    elif x == 1 and y == 2:
        directions1 = "(N)orth or (E)ast or (S)outh."
    elif x == 1 and y == 3:
        directions1 = "(E)ast or (S)outh."
    elif x == 2 and y == 1:
        directions1 = "(N)orth"
    elif x == 2 and y == 2:
        directions1 = "(W)est or (S)outh."
    elif x == 2 and y == 3:
        directions1 = "(W)est or (E)ast."
    elif x == 3 and y == 3: 
        directions1 = "(W)est or (S)outh."
    elif x == 3 and y == 2:
        directions1 = "(S)outh or (N)orth."
    elif x == 3 and y == 1:
        print("Victory!")
        return True
    print("You can travel: ", "{}".format(directions1))

def legal_moves(x, y, user_input):
    if x == 2 and y == 2 and (user_input == "n" or user_input == "e"):
        print("Not a valid direction!")
    elif (x == 1 and y == 1) and (user_input != "n"):
        print("Not a valid direction!")
    elif (x == 1 and y == 2) and (user_input == "w"):
        print("Not a valid direction!")
    elif (x == 1 and y == 3) and (user_input == "n" or user_input == "w"):
        print("Not a valid direction!")
    elif (x == 2 and y == 1) and ( user_input != "n"):
        print("Not a valid direction!")
    elif (x == 2 and y == 3) and (user_input == "n" or user_input == "s"):
        print("Not a valid direction!")
    elif (x==3 and y == 3) and (user_input == "n" or user_input == "e"):
        print("Not a valid direction!")
    elif (x == 3 and y == 2) and (user_input == "w" or user_input == "e"):
        print("Not a valid direction!") # breyta öllu í "not a valid"
    else:
        return False

    

x = 1
y = 1
while (x != 3 and y != 1) or (x < 4 and y < 4) :
    if instructions(x, y) == True:
        break
    user_input = input("Direction: ").lower()
    the_movement = movement(user_input, x, y)
    if legal_moves(x, y, user_input) != False:
        continue
    else:
        if (user_input == "w" or user_input == "e") and the_movement != 0 :   #Villa í boolean
            if user_input == "w":
                x -= 1
            else:
                x += 1
        elif (user_input == "n" or user_input == "s") and the_movement != 0:
            if user_input == "n":
                y += 1
            else:
                y -= 1
        
        elif the_movement == 0:
            continue
    












    