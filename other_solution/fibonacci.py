 # given an input, print out Fibonacci sequence
# get input from user 
inp = int(input("How many Fibonacci numbers would you like to see? "))
# create counter and number variables / need 2 number variables 
counter = 0
# first Fibonacci number 
num_one = 0
# second Fibonacci number 
num_two = 1
# counts the iterations of the loop from zero to input
while counter < inp:
    print(num_one) # print the first number
    num_three = num_one + num_two # make the third number the first number plus the second number
    num_one = num_two # make the first number equal the second number
    num_two = num_three # make the second number equal the third number
    counter += 1 # increment the counte