import random

money = 100

#Write your game of chance functions here
def heads_or_tails(face, bet):
    num = random.randint(1, 2)
    if ((num == 1) and (face == 'Heads')) or ((num == 2) and (face == 'Tails')):
        print('You won! Your winnings are $', bet*2)
        return bet*2
    else:
        print('You lost! You loose $', bet)
        return -bet
        

#Call your game of chance functions here
money += heads_or_tails('Heads',4)
print(money)
