import utils


# DSC = Decimal System Caster, this will work as a module for main .py file

# Function to cast a number when the base isn't 10
def cast(number, base):
    num_dec: int = 0
    steps = 0
    for num in utils.get_num_as_list(number, base):
        num_dec += num * (base ** steps)
        steps += 1
    return num_dec


# public function, call it to cast any base number to decimal system
def any_to_dec(number, base: int = 10):
    return number if base == 10 else cast(number, base)
