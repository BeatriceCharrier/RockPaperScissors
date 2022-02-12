import random
lists = ['rock', 'paper', 'scissors']
exit = ['!exit']
user_name = input('Enter your Name: ')
print(f'Hello, {user_name}')
counter_attack = None
action = input().split(',')
if action != ['']:
    lists = action
print("Okay, let's start")
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
        counter_attack = lists[lists.index(my_choose) + 1:]
        counter_attack += lists[:lists.index(my_choose)]
        counter_attack = counter_attack[:len(counter_attack) // 2]
        if bot_choose in counter_attack:
            print("Sorry, but the computer chose {}".format(bot_choose))
        elif my_choose == bot_choose:
            print("There is a draw ({})".format(my_choose))
            rating += 50
        else:
            print("Well done. The computer chose {} and failed".format(bot_choose))
            rating += 100