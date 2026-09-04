
computer_choice = 'scissors'
user_choice = input('Do you want rock, paper or scissors?')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('User Win!')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('User Win!')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('User Win!')
else:
    print('Computer Win!')