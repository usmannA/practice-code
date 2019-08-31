''' program that takes user input of two numbers to see if one can be wholly divisible by the other, if this isn't the case the remainder is printed'''


num = int(input("choose a number: "))
check = int(input("choose another to divide your first number with: "))

remainder = str (num % check) # had to turn to string in order to concatinate at end

if num % check == 0:
  print ("the second number you have chosen goes evenly into the first ")

else:
  print("the second number does not go evenly into the first")
  print ("the remainder is: " + remainder)
