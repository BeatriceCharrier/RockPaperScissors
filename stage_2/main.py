import random
lists = ['rock', 'paper', 'scissors']
bot_choose = random.choice(lists)

choose = input()

if choose == 'paper' and  bot_choose == 'scissors':
    print("Sorry, but the computer chose scissors")
elif choose == 'scissors' and bot_choose == 'rock':
    print("Sorry, but the computer chose rock")
elif choose == 'rock' and bot_choose == 'paper':
    print("Sorry, but the computer chose paper")

if choose == 'paper' and bot_choose == 'rock':
    print("Well done. The computer chose rock and failed")
elif choose == 'scissors' and bot_choose == 'paper':
    print("Well done. The computer chose paper and failed")
elif choose == 'rock' and bot_choose == 'scissors':
    print("Well done. The computer chose scissors and failed")

if choose == bot_choose:
    print(f"There is a draw ({choose})")