def name_of_function():
  ''' Docstring explains function ''' #optional, multiline string explains function, this is not exectued, just for someone else to read to explain what the function is suppose to do
  print ("hello")

  

#def = keyword telling python this is a function
#word_word = snakecasing(_)is all lowercase with underscores between words
# () Parenthesis at the end. We can pass arguments/parameters into the function
# : Colon indicates an upcoming indented block.Everything indented is then "inside" the function

def name_of_function(name):
  print ("hello " + name)

name_of_function ("David")
hello David

#functions can accepts arguments to be passed by the user

#---

def add_function (num1, num2):
    return num1 + num2 #we use return keyword to send back the result of the function instead of just printing out
result = add_function (2, 4) # return allows us to assign the output of the function to a new variable
result
6

