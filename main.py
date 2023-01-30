# Main function
import to_decimal_module


try:
    # create objects
    DSC = to_decimal_module
    entry = "312d"
    base = 14
    print(f'The value of {entry}({base}) = {DSC.any_to_dec(entry, base)}(10)')
except ValueError as e:
    print(f'Error: ${e}')
