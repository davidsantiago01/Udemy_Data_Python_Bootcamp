#Numbers: store numerical information and come into two forms:
    #Integers - whole numbers
    #Floating Point - Numbers with a decimal

#Strings: Ordered sequence of characters
#Lists: Ordered sequence of objects (mutable)
#Tuples: ordered sequence of objects (inmutable)
#Dictionaries: key-value pairing that is unordered

    #What is the value of the expression 4 * (6 + 5) = 44
    #What is the value of the expression 4 * 6 + 5 = 29
    #What is the value of the expression 4 + 6 * 5 = 34

#What is the *type* of the result of the expression 3 + 1.5 + 4?<br><br> = #float number

# Square root: 
81 ** 0.5 = 9.0
# Square:
9 ** 9 = 81

s = 'hello'
# Print out 'e' using indexing
print (s[1])

s ='hello'
# Reverse the string using slicing
print (s[::-1])

s ='hello'
# Print out the 'o'
# Method 1:
print (s[4])

# Method 2:
print (s[-1])

#List
# Method 1:
[1] * 3

# Method 2:
list1 = [1,2,3]
list1

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print (list3)

list4 = [5,3,4,6,1]
list4.sort()
print (list4)

#Dictionaries
d = {'simple_key':'hello'}
# Grab 'hello'
d = {'simple_key':'hello'}
print (d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print (d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
print (d['k1'][0]['nest_key'][1][0])

#Tuples
How do you create a tuple?<br><br>
tuple1 = (1, 2 ,3)

#Sets
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)

