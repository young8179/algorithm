def has_same_digit_frequency(x, y):
    y = sorted(y)
    if x == y:
        return True
    else:
        return False

list1 = [2, 4, 6, 8]
list2 = [8, 6, 4, 2]
result = has_same_digit_frequency(list1, list2)
print(result)

print("-----------------------------------")
def has_same_frequency(x, y):
    if len(x) != len(y):
        return False
    dict1 = {}
    for num in x:
        if num in dict1.keys():
            dict1[num] += 1
        else:
            dict1[num] = 1
    for num in y:
        if result[num] == 0:
            return False
        else:
            result[num] -= 1
    return True




print("-------------------------------------")

def same_digit_freq(a, b):
    if len(a) != len(b):
        return False
    else:
        a.sort(), b.sort()
        if a != b:
            return False
        else: 
            return True

print("------------------------------")

