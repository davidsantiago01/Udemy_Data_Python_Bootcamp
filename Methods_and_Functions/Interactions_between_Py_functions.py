
example = [1,2,3,4,5,6,7,8,9,10]
from random import shuffle
shuffle(example)
example
[2, 3, 1, 9, 6, 5, 4, 10, 7, 8]
#---

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
shuffle_list(example)
[8, 1, 6, 9, 5, 10, 7, 3, 4, 2]

#---

