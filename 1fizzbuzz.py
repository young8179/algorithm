'''Take a user's input for a number, and then print out all
numbers from 1 to that number. For any number
divisible by 3, print 'fizz'. For any number divisible by
5, print 'buzz'. Any number divisible by 3 AND 5, print
'fizzbuzz'. '''

# take user input num
user_input = input("give me number: ")
#print out all num 1 to user num
for number in range(1, int(user_input) + 1):    ##remove int and set start and end , + 1
    
    # check if divisible by 3 and 5
    # if yes, print fizzbuzz. if no print num
    if number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz")
# check if divisible by 3
# if yes , print fizz , if no, print num
    elif number % 3 == 0:
        print("buzz")
    
# check if divisible by 5
# if yes, buzz. if no, print num
    elif number % 5 == 0:
        print("fizz")

    
    else:
        print(number)

## try to use while

