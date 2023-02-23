def is_consecutive(a_list):
    """
    \nReturns True if all numbers in a list are consecutive or the list has
    only a single element. 
    \nReturns False if any two numbers are not consecutive
    or if the list is empty.
    """
    # At least 1 element defaults to True, empty lists will be False
    if a_list:
        flag = True
    else:
        flag = False

    # Flag stays True if each element is consecutive to the next element
    for index,object in enumerate(a_list[:-1]):
        if a_list[index+1] - a_list[index] == 1:
            flag = True
        elif a_list[index+1] - a_list[index] != 1:
            flag = False
            break
    
    # Function returns the final value of the flag
    if flag == True:
        return True
    elif flag == False:
        return False
    
my_list = [2,3,4,5,6,7]
print(my_list)
print(is_consecutive(my_list))

my_list_2 = [1,2,4,5]
print(my_list_2)
print(is_consecutive(my_list_2))