
user_input = input("type string: ")


dict1= {}
def string_count(string):
    
    for letter in string.lower():
        if letter in dict1:
            dict1[letter] += 1
        else:
            dict1[letter] = 1    
    return dict1

print(string_count(user_input))
# handle space
# if letter == " ":
    #continue