import random
lists = ['rock', 'paper', 'scissors']
exit = ['!exit']
while True:
    choose = input()
    if choose in exit:
        print("Bye!")
        break
    elif choose not in lists and exit:
        print("Invalid input")
        continue
    elif choose in lists:
        bot_choose = random.choice(lists)
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
            print("There is a draw ({})".format(choose))