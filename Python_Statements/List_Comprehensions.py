my_string = "hello"
my_list = []
for letter in my_string:
    my_list.append (letter)

my_list
['h', 'e', 'l', 'l', 'o']
#----

my_list = [letter for letter in my_string]

my_list
['h', 'e', 'l', 'l', 'o']

#----
my_list = [c for c in "Good Morning"]

my_list
['G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g']

#----
my_list = [num for num in range (0,11)]
my_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#----
my_list = [num**2 for num in range (0,11)]
my_list
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#---

