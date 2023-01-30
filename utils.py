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


# get the integer value of a number, auto transform A = 10...
def get_int_value(entry):
    entry = entry.upper() # uppercase in case of letter
    # try to cast to number
    try: # if is a number, will automatically cast
        return int(entry)
    except ValueError as e: # otherwise, is a letter, try to check if is into domain
        # get the ASCII Number of letter code minux 61 so is the value as integer
        if 60 < ord(entry) < 91:
            return ord(entry) - 55
        else:
            raise ValueError(f'Numeric system out of range for entry {entry}')
