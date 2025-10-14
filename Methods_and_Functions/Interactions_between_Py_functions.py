
example = [1,2,3,4,5,6,7,8,9,10]
from random import shuffle
shuffle(example)
example
[2, 3, 1, 9, 6, 5, 4, 10, 7, 8]
#---

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
result
[8, 1, 6, 9, 5, 10, 7, 3, 4, 2]

#---

my_list = [' ', 0, ' ']
shuffle_list(my_list)
[' ', ' ', 0]

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input ("Pick a number: 0, 1 or 2: ")
    return int(guess)
player_guess()
my_index = player_guess()
my_index

def check_guess(my_guess, my_list):
    if my_list[my_guess] == 0:
        print ("Correct!")
    else:
        print ("Wrong guess!")
        print (my_list)
my_list = [' ', 0, ' ']
mixedup_list = shuffle_list(my_list)
guess = player_guess()
check_guess(guess, mixedup_list)
#First attempt with #1
Correct!
#Second attempt with #0
Wrong guess!
[' ', ' ', 0]

#---------------





