# import call method from subprocess module
import os
from subprocess import call


# transform any number to a array of numbers
def get_num_as_list(number, base):
    data: list = []
    for num_s in f'{number}':
        num = get_int_value(num_s)
        if num < base:
            data.insert(0, num)  # check this, we flip the number at this point
            continue
        raise ValueError(f'The digit {num}[{number}] is higher than base {base}')
    return data


# transform any array of numbers to a single number
def get_list_as_num(data: list):
    return ''.join(data)


# get the integer value of a number, auto transform A = 10...
def get_int_value(entry):
    entry = entry.upper()  # uppercase in case of letter
    # try to cast to number
    try:  # if is a number, will automatically cast
        return int(entry)
    except ValueError as e:  # otherwise, is a letter, try to check if is into domain
        # get the ASCII Number of letter code minux 61 so is the value as integer
        if 64 < ord(entry) < 91:
            return ord(entry) - 55
        else:
            raise ValueError(f'Numeric system out of range for entry {entry}')


# cast from an int to ASCII, but only from A-Z son numbers [5,40] are valid
def cast_ascii(value):
    if 10 < value < 36:
        return chr(value + 55)
    else:
        raise ValueError(f'the number {value} is not valid for this system')


# return a letter if the number is higher tan 9, or a number if is between 0 and 9
def get_ascii_from_int(value):
    return value if 0 <= value < 10 else cast_ascii(value)


# clear window
# check and make call for specific operating system
# for mac and linux(here, os.name is 'posix') and windows 'cls'
def clear_screen():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')
