'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.'''


entered_number= int(input("Please enter any number:"))

if entered_number % 2 == 0:
  print ("Thats an even number")


if entered_number % 4 == 0:
  print("that's also a multiple of four")
  
else:
  print ("That's an odd number")
