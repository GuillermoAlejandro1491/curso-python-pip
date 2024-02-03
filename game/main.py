import random 

def choose_options():
    options = ('Rock', 'Paper', 'Scissors')
    user_option = input('Please choose your option ==> ').title()
    if not user_option  in options:
        print('Invalid Option')
        
        return None, None
    computer_option = random.choice(options)
    
    print('User option ==> ', user_option)    
    print('Computer option ==> ', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('DRAW')
    elif user_option == 'Rock' and computer_option == 'Scissors':
        print('User wins the round')
        user_wins += 1
    elif user_option == 'Scissors' and computer_option == 'Paper':
        print('User wins the round') 
        user_wins += 1 
    elif user_option == 'Paper' and computer_option == 'Rock':
        print('User wins the round')
        user_wins += 1
    elif computer_option == 'Scissors' and user_option == 'Paper':
        print('Computer wins the round')            
        computer_wins += 1
    elif computer_option == 'Paper' and user_option == 'Rock':
        print('Computer wins the round')
        computer_wins += 1
    elif computer_option == 'Rock' and user_option == 'Scissors':
        print('Computer wins the round')
        computer_wins += 1
    return user_wins, computer_wins

def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1
    while True:
        print('*' * 20)
        print('ROUND', rounds)
        print('*' * 20)
        
        print('User_wins = ', user_wins)
        print('Computer_wins = ', computer_wins)
        
        rounds += 1
        
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if computer_wins == 2:
            print('THE WINNER IS COMPUTER!!!!')
            break
        
        if user_wins == 2:
            print('THE WINNER IS USER!!!')
            break
run_game()            