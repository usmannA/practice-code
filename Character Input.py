'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
'''


name = input ("What is your name?")
age = int(input ("what is your age?"))
random = int(input ("choose any random rumber between 1-100"))

C = (100- age)
D = str(2019+ C)

X = ("Hi " + name + ", You could turn 100 in the year " + D+".")

print (X*random)
