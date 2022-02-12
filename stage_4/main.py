import random
lists = ['rock', 'paper', 'scissors']
exit = ['!exit']
user_name = input('Enter your Name: ')
print(f'Hello, {user_name}')
rating_file = open("rating.txt")
rating = 0
for line in rating_file:
    name, score = line.split(" ")
    if name == user_name:
        rating = int(score)

while True:
    my_choose = input()
    if my_choose in exit:
        print("Bye!")
        break
    elif my_choose == '!rating':
        print('Your rating: ' + str(rating))
        continue
    elif my_choose not in lists and exit:
        print("Invalid input")
        continue
    elif my_choose in lists:
        bot_choose = random.choice(lists)
        if my_choose == 'paper' and  bot_choose == 'scissors':
            print("Sorry, but the computer chose scissors")
        if my_choose == 'scissors' and bot_choose == 'rock':
            print("Sorry, but the computer chose rock")
        if my_choose == 'rock' and bot_choose == 'paper':
            print("Sorry, but the computer chose paper")

        if my_choose == 'paper' and bot_choose == 'rock':
            print("Well done. The computer chose rock and failed")
            rating += 100
        if my_choose == 'scissors' and bot_choose == 'paper':
            print("Well done. The computer chose paper and failed")
            rating += 100
        if my_choose == 'rock' and bot_choose == 'scissors':
            print("Well done. The computer chose scissors and failed")
            rating += 100
    
        if my_choose == bot_choose:
            print("There is a draw ({})".format(my_choose))
            rating += 50