inp = input('Give me a string: ').lower()
def most_characters(str):
  if len(str) == 0:
    print('Empty String')
  result = {}
  letter_count = 0
  for letter in str:
    if letter not in result:
      result[letter] = 1
    else:
      result[letter] += 1
  for value in result.values():
    if value > letter_count: 
      letter_count = value
  for key in result.keys():
    if result[key] == letter_count:
      print(f'{key}: {result[key]}')
most_characters(inp)


print("---------------------------")

# write a function called most_characters that accepts a string, and return the character that appears the most.
# so most_characters("abcda") should return "a"

def most_characters(string):
    # short circuit
    # if len(str) == 0:
    #     print('You entered an empty string')
    dictionary = {}
    # loop through the string, the char doesn't exist as a key already in the dictionary
    # then it adds that char as a key and initializes its value as 1
    for char in string.lower():
        if char not in dictionary:
            dictionary[char] = 1
        else: # if it already exists, then it adds one to the value
            dictionary[char] += 1
    
    # list to house the highest frequency and the respective character
    highest_frequency = [0, '']
    for key in dictionary:
        if dictionary[key] > highest_frequency[0]:
            highest_frequency[0] = dictionary[key]
            highest_frequency[1] = key
        elif dictionary[key] == highest_frequency[0]:
            highest_frequency[1] += f' and {key}'
    
    return highest_frequency


print(f'\n\nChar(s) with the highest frequency: \n{most_characters("Bannanna")[1]}\nWith a frequency of:\n{most_characters("Bannanna")[0]}\n\n')
# print(most_characters("Gerrit"))








