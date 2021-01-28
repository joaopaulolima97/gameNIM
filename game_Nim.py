print('Welcome to Nim Game!')
print('Please, choose the options below:')
print('')
    
def computer_chooses(n,m):
    #x=pieces that the computer will pick up 
    #n=total of pieces
    #m=pieces allowed to be taken per round
    x=0
    x=n-(m+1)
    if n%m==1:
        x=1
        return x
    if x>0 and x<m:
        return x
    if x<0:
        return n
    if n%m==0:
        x=1
        return x        
    else:
        return m
    
def user_chooses(n,m):
    y=int(input('How many pieces are you going to take out? '))
    if y>=1 and y<=m:
        return y  
    else:
        while y<1 or y>m:
            print('')
            print('Oops! Invalid move! Try again. ')
            y=int(input('How many pieces are you going to take out?'))
        return y
          
def match():
    n=int(input('How many pieces?'))
    m=int(input('Limit of pieces per move?'))
    while n<m:
        print('Invalid numbers, try again! !')
        n=int(input('How many pieces?'))
        m=int(input('Limit of pieces per move?'))    
    user_play=False 
    if n%(m+1)==0:
        user_play=True
        print('')
        print('You start!')
    else:
        print('')
        print('Computer start!')
    
    while n>0:
        if user_play==True:
            y=user_chooses(n,m)
            n=n-y
            if y==1 and n>1:
                print('\nYou took out a piece.')
                print('Now {} pieces remain on the board.'.format(n))          
            if y==1 and n==1:
                print('\nYou took out a piece.')
                print('Now one piece remain on the board.')
            if y>1:
                if n>1:
                    print('\nYou took out {} pieces.'.format(y))
                    print('Now {} pieces remain on the board.'.format(n))
                else:
                    print('\nYou took out {} pieces.'.format(y))
                    print('Now one piece remain on the board.')
                    
            user_play=False
            
        else:
            x=computer_chooses(n, m)
            n=n-x
            if x==1 and n==0:
                print('\nThe computer took a piece.')
                print('End of the game! The Computer has won!')  
            if x==n and n==0:
                print('\nThe computer took {} pieces.'.format(x))
                print('End of the game! The Computer has won!')                  
            if x==1 and n>1:
                print('\nThe computer took a piece.')
                print('There are {} pieces left on the board.'.format(n))
            if x==1 and n==1:
                print('\nThe computer took a piece.')
                print('There are {} pieces left on the board.'.format(n))                 
            if x>1:
                if n==0:
                    print('\nThe computer took {} pieces.'.format(x))
                    print('End of the game! The Computer has won!')
                else: 
                    print('\nThe computer took {} pieces.'.format(x))
                    print('There are {} pieces left on the board.'.format(n))     
            user_play=True  

def championship():
    # Composed of 3 matches
    Round=1
    while Round<=3:
        print('')
        print('**** Round {} ****'.format(Round))
        print('')
        match()
        Round=Round+1
    print('')
    print('**** End of Championship! ****')
    print('')
    print('Score: You 0 X 3 Computer')

def main():
    print('1 - To play just one game' )
    choose=int(input('2 - To play a championship: '))   
    if choose==1:
        print('You chose a single match!')
        match()
    if choose==2:
        print('\nYou chose a championship!')
        championship()
    else:
        while choose!=1 and choose!=2:
            print('\nInvalid number! Try again.\n')
            print('1 - To play just one game' )
            choose=int(input('2 - To play a championship'))   
            if choose==1:
                print('\nYou chose a single match!')
                match()
            if choose==2:
                print('\nYou chose a championship!')
                championship()

print(main())