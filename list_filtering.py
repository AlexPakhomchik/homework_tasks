# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list
# with the strings filtered out.

def filter_list(l):
    new_list = []
    for i in l:
        if type(i) == int and i >= 0:
            new_list.append(i)

    return new_list
