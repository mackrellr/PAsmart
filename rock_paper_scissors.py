import random

player_choice = 0
npc_choice = 0
game_on = True

    
# Indicate choices for win
def choices(p1, p2):
    print()
    if p1 == 1:
        print('Player choose Rock.')
    if p1 == 2:
        print('Player choose Paper.')
    if p1 == 3:
        print('Player choose Scissors.')

    if p2 == 1:
        print('Opponent choose Rock.')
    if p2 == 2:
        print('Opponent choose Paper.')
    if p2 == 3:
        print('Opponent choose Scissors.')

def winner(p1, p2):
    # Rock (1) beats scissors (3)
    if p1 == 1 and p2 == 3:
        print('You win. Rock crushes scissors.')
    if p2 == 1 and p1 == 3:
        print('You loose. Rock crushes scissors.')

    # Scissors (3) beats paper (2)
    if p1 == 3 and p2 == 2:
        print('You win. Scissors cuts paper. ')
    if p2 == 3 and p1 == 2:
        print('You loose. Scissors cuts paper.')
        
    # Paper (2) beats rock (1)
    if p1 == 2 and p2 == 1:
        print('You win. Paper covers rock.')
    if p2 == 2 and p1 == 1:
        print('You loose. Paper covers rock.')

    # Indicate a tie
    if p1 == p2:
        choices = ['rock', 'paper', 'scissors']
        print('Tie. You both choose ' + choices[p1-1] + '.')

#Loop the game until a specified number of wins
while game_on:
    # Player input
    choice_bank = input('Rock [1], paper [2], scissors [3], shoot! ')
    if choice_bank != '1' and choice_bank != '2' and choice_bank != '3':
        print('Incorrect entry, please choose: ')
    else:
        player_choice = int(choice_bank)

        # Random computer input
        npc_choice = random.randrange(1, 4)
    
        choices(player_choice, npc_choice)
        winner(player_choice, npc_choice)
        
        # Offer to exit the game
        game_quit = True
        while game_quit:
            exit_game = input('Would you like to play again y/n? ')
            if exit_game == 'n':
                print('Thank you for playing!')
                game_quit = False
                game_on = False
            elif exit_game != 'y' and choice_bank != 'n':
                print('Incorrect entry.')
            elif exit_game == 'y':
                game_quit = False
                game_on = True 
    

