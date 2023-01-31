import backend.modules.FromDecimalModule as FDM
import backend.modules.ToDecimalModule as TDM
import backend.utils.utils as utils


# Main function

def cast():  # Objective, cast any number from any base to another base
    try:
        # variables
        entry = input('Numero: ')
        base = int(input('Base: '))
        target_base = int(input('Base objetivo: '))

        # check bases
        if 1 < base < 37 and 1 < target_base < 37:
            # calc results
            decimal = TDM.any_to_dec(entry, base)
            output = FDM.dec_to_any(decimal, target_base)

            # results
            print(f'The value of {entry}({base}) = {decimal}(10)')
            print(f'The value of {decimal}(10) = {output}({target_base})')
        else:
            print(f'Una(s) de las(s) bases es o son invalidas, revisa que esten en el rango [2,36]')
    except ValueError as e:
        print(f'Error while running application: {e}')


def menu():  # infinite loop with main menu
    while True:
        print(f'=======================\n\tMENU\t\n0. Salir\n1. Convertir bases\n')
        try:
            status_code = int(input('Selecciona una opción: '))
            if status_code == 0:
                break
            elif status_code == 1:
                cast()
            else:  # clear screen
                utils.clear_screen()
                print('-> OPCION INVALIDA <-')
        except ValueError as e:
            print('Valor invalido...')
    print('FIN DEL PROGRAMA')


# run code
menu()