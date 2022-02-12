rock = "rock"
scissors = "scissors"
paper = "paper"

choice = str(input())
if choice == scissors:
    print(f'Sorry, but the computer chose {rock}')
elif choice == rock:
    print(f'Sorry, but the computer chose {paper}')
elif choice == paper:
    print(f'Sorry, but the computer chose {scissors}')