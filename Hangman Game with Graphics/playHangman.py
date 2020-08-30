from cs1graphics import*
from hangmanGraphics import*
secret = input("Please put in a secret word: ")
def playHangman(secret):
    paper = Canvas(600,600, 'white', "HANGMAN-GAME")
    secreT = secret.upper() #making the secret number all capital
    completion_list = list('_'*len(secret))   #creating the list of the player progress
    secret_list = list(secreT)     # creating a list of secret words _completion and secret list will obviously have the same length
    wrong_list = []             #Creating a list of wrong words
    correct_list = []           #Cretating a list of correct words
    n_guess = 0                 #the number of wrong guess the user is trying
    
    print("Go ahead and start guessing. Good Luck!")
    print(' '.join(completion_list))
    print()
    status = False
    alphabets_list = list('abcdefghijklmnopqrstuvwxyz')
    while n_guess <10 and status == False:
        guess_ = input('Guess an alphabet: ')
        while  guess_ not in alphabets_list: 
            guess_ = input('Please make sure your guess should only on be one alphabet: ')
        guess = guess_.upper()
        if guess in correct_list:
            print (f"You already have the character {guess} correct")
            print(' '.join(completion_list))
        elif guess in secret_list:
            correct_list.append(guess)
            i=0
            for k in secret_list:
                if k == guess:
                    completion_list[i]= guess
                i+=1
            print()
            print(' '.join(completion_list))
            print()
            print('WRONG CHARACTERS: ',','.join(wrong_list))
            if completion_list == secret_list:
                status = True
        elif guess in wrong_list:
            print()
            print (f"You already have the character {guess} wrong")
            print(' '.join(completion_list))
            print()
            print('WRONG CHARACTERS: ',','.join(wrong_list))
            print()
        else:
            n_guess+=1
            wrong_list.append(guess)
            if n_guess == 1:
                paper.add(ground())
            elif n_guess == 2:
                paper.add(standing_pole())
            elif n_guess==3:
                paper.add(up_pole())
            elif n_guess==4:
                paper.add(rope())
            elif n_guess == 5:
                paper.add(head())
            elif n_guess == 6:
                paper.add(body())
            elif n_guess == 7:
                paper.add(left_hand())
            elif n_guess == 8:
                paper.add(right_hand())
            elif n_guess == 9:
                paper.add(left_leg())
            elif n_guess == 10:
                paper.add(right_leg())
            print(f"You have {10-n_guess} more trials")
            print()
            print('WRONG CHARACTERS: ',','.join(wrong_list))
            print()
            print(' '.join(completion_list))
            if n_guess ==10:
                print()
    if status == True:
        print('CONGRATS YOU WON THE GAME!!!')
    elif status == False:
        print('GAME OVER YOU LOST')
    ask_ = input('Do you want to play this game again:' )
    ask =  ask_.lower()
    if ask in ['yes','y','yah','yh','yoh', 'yea']:
        secret_word = input("Pleae type in a secret word: ")
        while len(secret_word)<=1:
            secret_word = input("Pleae type in a secret word: ")
        playHangman(secret_word)
    else:
        print ("Thank you for playing this game! See you soon")
#x = 'Moubarack'
#playHangman(x)
