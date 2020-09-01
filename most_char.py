
def most_characters(string):
    dict_1 = {}
    #put all letter into dict and count
    
    for letter in string:
        if letter in dict_1:
            dict_1[letter] += 1
        else:
            dict_1[letter] = 1  
    #pick the most number(value)
    most_count = max(dict_1, key=dict_1.get)
    print(most_count)

input_string = "bAnAna"
most_characters(input_string)

print("----------------------------------")

