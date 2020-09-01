def has_same_digit_frequency(list1, list2):
    dict1 = {}
    dict2 = {}
 
    
   
    for item in list1:
        if item in dict1.keys():
            dict1[item] += 1
        else:
            dict1[item] = 1
 
    for item in list2:
            if item in dict2.keys():
                dict2[item] += 1
            else:
                dict2[item] = 1
    
    for values in dict1.items():
        if dict1 == dict2:
            return True
        else:
            return False
 
 
print(has_same_digit_frequency([1,2,3,4],[1,2,3,4]))
print(has_same_digit_frequency([5], [7,8]))
 