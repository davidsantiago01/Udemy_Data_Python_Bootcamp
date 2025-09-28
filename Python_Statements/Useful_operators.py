my_list = [1, 2, 3]
my_list = [1,2,3]
for num in range(3,10):
    print (num)
3
4
5
6
7
8
9
#---

index_count = 0
for letter in "abcde":
    print ("At index {} the letter is {}".format(index_count,letter))
    index_count = index_count + 1
At index 0 the letter is a
At index 1 the letter is b
At index 2 the letter is c
At index 3 the letter is d
At index 4 the letter is e
#---

word ="abcde"

for item in enumerate (word):
    print (item)

(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')

#---

word ="abcde"

for index,item in enumerate (word):
    print (index)
    print (item)
    print ("\n")

0
a


1
b


2
c


3
d


4
e
#---

my_list1 = [1,2,3]
my_list2 = ["a","b","c"]

for item in zip (my_list1,my_list2):
    print (item)
(1, 'a')
(2, 'b')
(3, 'c')
#---
list (zip (my_list1,my_list2))
[(1, 'a'), (2, 'b'), (3, 'c')]
#---
"x" in [1,2,3]
False
#---
"x" in ["x","y","z"]
True
#---
"mykey" in {"mykey":345}
True
#---
d = {'mykey':345}
345 in d.values()
True
#---
my_list = [10, 20, 30, 40, 50, 100]
min(my_list)
#---
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle (mylist)
mylist
[2, 9, 3, 1, 5, 6, 10, 7, 8, 4]
#---
result = int(input ("Enter a number here: "))
result
20
