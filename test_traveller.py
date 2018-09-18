x = 1 
y = 1

while (0 < x < 4) and (0 < y < 4):
    if x == 1 and y == 1:
        directions = "(N)orth"
    elif x == 1 and y == 2:
        directions = "(N)orth or (E)ast or (S)outh"
    elif x == 1 and y == 3:
        directions = "(E)ast or (S)outh"
    elif x == 2 and y == 1:
        directions = "(N)orth"
    elif x == 2 and y == 2:
        directions = "(W)est or (S)outh"
    elif x == 2 and y == 3:
        directions = "(W)est or (E)ast"
    elif x == 3 and y == 3: 
        directions = "(E)ast or (S)outh"
    elif x == 3 and y == 2:
        directions = "(N)orth or (S)outh"
    elif x == 3 and y == 1:
        print("Victory!")
        break
    print("You can travel:", directions)
    move = input("Direction: ")
    if move == "n" and y != 3:
        movement = 1
    elif move == "e" and x != 3:
        movement =  1
    elif move == "s" and y != 1:
        movement = -1 
    elif move == "w" and x != 1:    
        movement = 1
    else:
        movement = 0
    if movement == 0:
        print("Invalid input!")
        continue
    
    
