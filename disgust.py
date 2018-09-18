start = (1,1)

way = '(N)orth.'
print('You can travel:',way)

while start != (3,1):
    
    if start == (1,1):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            start = (1,2)
            way = '(N)orth or (E)ast or (S)outh.'
            print('You can travel:',way)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start

    if start == (1,2):
        if direction == 'n' or direction =='N':
            start = (1,3)
            way = '(E)ast or (S)outh.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        elif direction == 'E' or direction =='e':
            start = (2,2)
            way = '(S)outh or (W)est.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        elif direction == 's' or direction =='S':
            start = (1,1)
            way = '(N)orth.'
            print('You can travel:',way)
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (1,3):
        if direction == 's' or direction == 'S':
            start = (1,2)
            way = '(N)orth or (E)ast or (S)outh.'
            print('You can travel:',way)
            direction = input('Direction: ')
        elif direction == 'e' or direction =='E':
            start = (2,3)
            way = '(E)ast or (W)est.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')


    if start == (2,2):
       
        if direction == 's' or direction == 'S':
            start = (2,1)
            way = '(N)orth.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        elif direction == 'w' or direction == 'W':
            start = (1,2)  
            way = '(N)orth or (E)ast or (S)outh.'
            print('You can travel:',way)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (2,1):
        
        if direction == 'n' or direction =='N':
            start = (2,2)
            way = '(S)outh or (W)est.'    
            print('You can travel:',way)
            direction = input('Direction: ')    
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (2,3):
        
        if direction == 'e' or direction =='E':
            start = (3,3)
            way = '(S)outh or (W)est.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        elif direction == 'w' or direction =='W':
            start = (1,3)
            way = '(E)ast our (S)outh.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (3,3):
       
        if direction == 'w' or direction =='W':
            start = (2,3)
            way = '(E)ast or (W)est.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        elif direction == 's' or direction == 'S':
            start = (3,2)
            way = '(N)orth or (S)outh.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (3,2):
    
        if direction == 's' or direction == 'S':
            start = (3,1) 
        elif direction == 'n' or direction == 'N':
            start = (3,3)
            way = '(S)outh or (W)est.'    
            print('You can travel:',way)
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            start = start
            direction = input('Direction: ')

    if start == (3,1):
        print('Victory!')