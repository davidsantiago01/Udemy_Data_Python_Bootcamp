while some_boolean_condition_
  do_something
else:
  do_something_different
--
x = 0
while x < 5:
  print (f'the current value of x is {x}')

  x+= 1
else:
    print ("X IS NOT LESS THAN 5")
the current value of x is 0
the current value of x is 1
the current value of x is 2
the current value of x is 3
the current value of x is 4
X IS NOT LESS THAN 5
--
mystring = "Sammy"
for letter in mystring:
    if letter == "a":
        continue
    print (letter)
S
m
m
y
--

mystring = "Sammy"
for letter in mystring:
    if letter == "a":
        break
    print (letter)
S
--
x = 0
while x < 5:
  if x == 2:
      break
  print (f'the current value of x is {x}')
  x += 1
the current value of x is 0
the current value of x is 1

