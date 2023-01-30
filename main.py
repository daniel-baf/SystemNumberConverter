# Main function
import to_decimal_module
import from_decimal_module

try:
    # create objects
    DSC = to_decimal_module
    FDM = from_decimal_module

    # Objective, cast 143(5) to base 8
    # 143 -> 48 -> 60
    entry = "51C231A"
    base = 16
    target_base = 36
    decimal = DSC.any_to_dec(entry, base)
    output = FDM.dec_to_any(decimal, target_base)

    # results
    print(f'The value of {entry}({base}) = {decimal}(10)')
    print(f'The value of {decimal}(10) = {output}({target_base})')
except ValueError as e:
    print(f'Error: {e}')
