# function to cast from decimal to any base
from backend.utils import utils


def dec_to_any(number, target_base):
    try:
        result: list = []
        get_value(number, target_base, result)
        str_final = "";
        for item in result:
            str_final += f'{utils.get_ascii_from_int(item)}'
        return str_final
    except ValueError as e:
        print(f'Unable to recover from error casting to a new base, {e}')
        raise e


# uses the formula N // B = a : b -> b // B = a1 : b1... and final number is an a_(n-1) a_(n-2) ... a_(n-m)
# N // B = a : b
# b // B = a1 : b1
# ... | a_n = carry b_n = partial result
# an = 0
def get_value(number, base, result: list):
    try:
        a_n = int(number // base)  # this is the left part of  a : b in N // B
        b_n = int(number - base * a_n)  # this is the right part of  a : b in N // B
        result.insert(0, b_n)
        if a_n != 0: get_value(a_n, base, result)
    except ValueError as e:
        print(f'Unexpected error un recursive method to cast {number}({base}) {e}')
