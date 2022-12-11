# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    new_digit_str = ''
    num_s = str(num)
    for n in range(len(num_s)):
        new_digit_str += str((int(num_s[n]))**2)
    return int(new_digit_str)

