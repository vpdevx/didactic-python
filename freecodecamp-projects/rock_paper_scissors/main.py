import random 

def play():
    user = input("Type 'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
        return 'tie'

    if is_win(user, computer):
        return "congrats!"

    return 'you lost!'

    # r > s, s > p, p > r

def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())