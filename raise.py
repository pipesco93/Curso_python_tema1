def palindrome(string):
    try:
        if len(string) == 0:
            #elevar una un error de tipo valueerror si longitud de string = 0
            raise ValueError("no se puede ingresar una cadena vacía")
        return string == string[::-1]
        #VE nombre variable value error, quiere decir qeu si ingreso cadena vcía imprime el valueerror
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar strings")
    


if __name__=='__main__':
    run()
