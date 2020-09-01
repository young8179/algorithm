'''Write a program that asks the user for a numerical
input,
'n'
, and prints out the next 'n' numbers of the
fibonacci sequence. (1, 1, 2, 3, 5, 8, 13, 21, 34...) '''

## take input

user_input = int(input("give me number: "))


number_1 = 1
number_2 = 1
count = [number_1, number_2]


for index in range(user_input-2):
    number_n = count[index] + count[index + 1]
    count.append(number_n)
print(count)

