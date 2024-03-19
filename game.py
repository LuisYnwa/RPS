import random

def play():
    computer = random.choice(['R', 'S', 'P'])
    player = input(" Please select between 'R' for rock, 'S' for scissors or 'P' for paper: ").upper
    print(computer)

    if player == computer:
        print('You both tied!')

    elif player_win(player, computer):
        print(f'The computer choose {computer_reveal(computer)}\n You won!!! :D')

    return f'The computer choose: {computer_reveal(computer)}\nYou lost! :('

def player_win(user, opponent):
    if user == 'R' and opponent == 'S' or user == 'S' and opponent == 'P' or user == 'P' and opponent == 'S':
        return True 
    
def computer_reveal(l):
    if l == 'R':
        l = 'Rock'
    elif l == 'S':
        l = 'Scissors'
    elif l == 'P':
        l == 'Paper'

print(play())