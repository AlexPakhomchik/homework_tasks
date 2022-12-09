# Create a function that moves all 0 to the right for a giving list:
#
# Example:
#
# prepare_list([1, 2, 3, 0, 4, 0, 0, 5])  # output: [1, 2, 3, 4, 5, 0, 0, 0]



def right_zero(list: list):
    new_list = []
    zero = []
    while 0 in list:
        for i in list:
            if i == 0:
                zero.append(list.pop(list.index(i)))
    new_list.extend(list)
    new_list.extend(zero)
    return new_list



a = [0, 0, 0, 1, 6, 2, 3, 9, 2, 0 , 0, 4, 5, 6]

list = right_zero(a)
