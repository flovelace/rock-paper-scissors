import random

def play():
    user = input("Choose: 'r' for rock, 'p' for paper, and 's' for a scissor!")
    computer = random.choice(['r', 'p', 's']) # select a random choice from the array

    if user == computer:
        return 'It\'s a tie!'
    
    if is_winner(user, computer):
        return 'Congratulations! You won!'
    # we just need a return statement here because if neither of the above conditions are met then the computer won
    return 'You lost! You are not a winner.'
    


def is_winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

    