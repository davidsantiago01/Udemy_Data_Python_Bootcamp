My_iterable = [1,2,3]
for item_name in My_iterable:
  print (item_name)
1
2
3

--

my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    print (num)
1
2
3
4
5
6
7
8
9
10
--

for num in my_list:
    if num % 2 == 0:
        print (num)
    else:
        print (f"Odd Number: {num}")
Odd Number: 1
2
Odd Number: 3
4
Odd Number: 5
6
Odd Number: 7
8
Odd Number: 9
10

--

list_sum = 0
for num in my_list:
    list_sum = list_sum + num

  print (list_sum)
1
3
6
10
15
21
28
36
45
55
--
tup = (1,2,3)
for item in tup:
  print (item)
1
2
3
--
my_list = [(1,2), (3,4), (5,6), (7,8)]
len (my_list)
4
--

for item in my_list:
    print (item)
(1, 2)
(3, 4)
(5, 6)
(7, 8)
--


