secret_number = 9
guess_count = 0
while guess_count < 3:
    if int(input('Guess nummber: ')) == 9:
        print("You win!")
        break
    guess_count = guess_count + 1
else:
    print("You failed!")
