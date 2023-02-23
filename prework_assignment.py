### Python Pre-Work Assignment: Harry Hill ###

## 1. Write a function to print "hello_USERNAME!" 
    # USERNAME is the input of the function.
    # The first line of the code has been defined as below:
    # def hello_name(user_name):

def hello_name(user_name):
    """Prints "hello_(user_name)!" """
    print(f"hello_{user_name}!")

hello_name("USERNAME")

## 2. Write a python function, first_odds that prints the odd numbers
    # from 1-100 and returns nothing
    # def first_odds():

def first_odds():
    """Prints the odd numbers from 1-100 and returns nothing."""
    for value in range(1,101):
        if value % 2 != 0:
            print(value)
        else:
            continue

first_odds()
print(first_odds())

## 3. Please write a Python function, max_num_in_list to return the max number
    # of a given list. 
    # The first line of the code has been defined as below:
    # def max_num_in_list(a_list):

def max_num_in_list(a_list):
    """Returns the max number of a given list."""
    return(max(a_list))

my_list = [1,2,3,4,5]
print(max_num_in_list(my_list))

## 4. Write a function to return if the given year is a leap year.
    # A leap year is divisible by 4, but not divisible by 100,
    # unless it is also divisible by 400. 
    # The return should be boolean Type (true/false).
    # def is_leap_year(a_year):

def is_leap_year(a_year):
    """Returns True if the given year is a leap year."""
    # Leap years are always divisible by 4 and are indivisible by 100 
    # unless they are divisible by 400
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2000))

## 5. Write a function to check to see if all numbers in list are
    # consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
    # but [1,2,4,5] are not consecutive numbers. 
    # The return should be boolean Type.
    # def is_consecutive(a_list):

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