'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(lst1, lst2):
    dct = {}
    for i in range(len(lst1)): 
        if i < len(lst2): 
            dct[lst1[i]] = lst2[i] 
        else:
            dct[lst1[i]] = None
    print(dct)

# two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}


'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''

def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    total = 0
    for i in range(start,(end+1)):
        if i < len(lst):
            total += lst[i]
    return total

# print(range_in_list([1,2,3,4],0,2))
# print(range_in_list([1,2,3,4]))

'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1, num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
    for key, val in d1.items():
        if not key in d2.keys():
            return False
        elif d1[key] != d2[key]:
            return False
    return True

# print(same_frequency(551122,221515))

'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

def min_max_key_in_dictionary(dct):
    min_key = min(list(dct))
    max_key = max(list(dct))
    return [min, max]
    
# print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))

'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(lst1):
    count = 0
    for num1 in lst1:
        # print(num1)
        index = lst1.index(num1)
        # print(index)
        lst2 = lst1[index+1:]
        # print(lst2)
        for num2 in lst2:
            if num1 < num2:
                count += 1
    return count

# print(find_greater_numbers([1,2,3]))

'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''

def two_oldest_ages(lst):
    oldest_1 = max(lst)
    lst.remove(oldest_1)
    oldest_2 = max(lst)
    return [oldest_2, oldest_1]


# two_oldest_ages( [4,25,3,20,19,5] )