import random

print 'I am thinking of a number between 1 and 10'
user_guess = int(raw_input('What is the number? '))

my_rand_number = random.randint(1, 10)
num_of_guesses = 5

while user_guess != my_rand_number:
    for x in range(0,4):
        if user_guess > my_rand_number:
            num_of_guesses -= 1
            print 'You are too high'
            print 'You have %s guesses left.' % (num_of_guesses)
            user_guess = int(raw_input('What is the number? '))

        elif user_guess < my_rand_number:
            num_of_guesses -= 1
            print 'You are too low'
            print 'You have %s guesses left.' % (num_of_guesses)
            user_guess = int(raw_input('What is the number? '))

        else:
            break

    break

if user_guess == my_rand_number:
    print 'You have chosen wisely.'
else:
    print 'You ran out of guesses.'
