
'''
Given an integer, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''

x = int(input("type a number: ")) 

if (x % 2) > 0:
    print ("Weird")

elif ((x % 2) == 0) and (x>=2 and x<=5):
    print ("Not Weird")


elif ((x % 2) == 0) and (x>=6 and x<=20):
    print ("Weird")

elif (x % 2) == 0 and x>20:
    print ("Not Weird")
