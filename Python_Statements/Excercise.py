st = "Print only the words that start with s in this sentence"
for word in st.split():
    if word [0] == "s":
        print (word)
start
s
sentence

#---
for num in range (0, 11, 2):
    print (num)
0
2
4
6
8
10
#---

[x for x in range (1,51) if x % 3 == 0]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

#---
my_list = []
for x in range (1, 51):
     if x % 3 == 0:
          my_list.append (x)
my_list
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
#---

st = "Print every word in this sentence that has an even number of letters"
for word in st.split():
    if len(word) % 2 == 0:
        print (word + " is even!")
word is even!
in is even!
this is even!
sentence is even!
that is even!
an is even!
even is even!
number is even!
of is even!
#---

for num in range (0, 101):
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
FizzBuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz

#---

st = "Create a list of the first letters of every word in this string"

for word in st.split():
    print (word[0])
C
a
l
o
t
f
l
o
e
w
i
t
s


