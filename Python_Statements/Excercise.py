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


