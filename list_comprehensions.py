from typing import Sequence


def run():

    # # Lista con cuadrdo de los primeros 100 numero snaturales
    # squares = []
    # for i in range(1, 101): # el ultimo parametro no es inclusivo
    #     if i % 3 != 0: # Solo voy a guardar el cuadrado de los números que no son divisible entre 3
    #         squares.append(i**2)

# Hcer lo que esta comentado con lists comprehensiosns
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    multiplos = [m for m in range(1, 10001) if m % 4 == 0 and m % 6 == 0 and m % 9 == 0 ]
    print (multiplos)




if __name__=='__main__':
    run()