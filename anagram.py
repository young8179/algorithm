



def anagram(word_1, word_2):
    first_word_dict = {}
    second_word_dict = {}
    for letter in word_1.lower():
        if letter == " ":
            continue
        if letter in first_word_dict:
            first_word_dict[letter] +=1
        else:
            first_word_dict[letter] = 1
    for letter in word_2.lower():
        if letter == " ":
            continue
        if letter in second_word_dict:
            second_word_dict[letter] +=1
        else:
            second_word_dict[letter] = 1
    
    print(first_word_dict)
    print(second_word_dict)
    return first_word_dict == second_word_dict
    

print(anagram("Funeral", "real fun"))