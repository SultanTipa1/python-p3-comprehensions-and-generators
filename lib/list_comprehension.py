# sys allows us to look into system memory, among other things
import sys
#!/usr/bin/env python3

def return_evens(num_list):
    # use list comprehension to filter out even numbers
    evens = [num for num in num_list if num % 2 == 0]
    return evens # Ensure that a list is always returned
    #return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    # check if the sentence list is not empty
    if sentence_list:
        return [sentence + "!" for sentence in sentence_list]
    else:
        return [] # Return an empty list if input is empty








# squared_minus_one = list()

# for n in range (1, 11):
#     squared_minus_one.append((n ** 2) - 1)

# print(squared_minus_one)

# [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]

# Syntax for list comprehension

# new_list = [optional_operation(item) for item in old_list if optional_condition == True]


# Generator Expressions


# one_to_three = range(1, 4)

# Alist comprehension uses square brackets

# squared_lc = [n ** 2 for n in one_to_three]

# A generator expression uses parentheses
# squared_ge = (n ** 2 for n in one_to_three)

# looping through all  show identical values...
# for n in squared_lc:
#     print(n)

# 1
# 4
# 9

# for n in squared_ge:
#     print(n)

# 1
# 4
# 9

# But the ojects are not identical

# print(squared_lc)

# [1, 4, 9]

# print(squared_ge)

# <generator object <genexpr>>

# list_comprehension = [n for n in range(100000)]
# generator_expression = (n for n in range(100000))

# # Returns the size of an object in bytes
# sys.getsizeof(list_comprehension)
# # 824456

# sys.getsizeof(generator_expression)
# 112