def palindrome(string):
    return string == string[::-1]

def run():
    try:
        print(palindrome(1))
    except TypeError:
        print("Solo se pueden ingresar strings")
    


if __name__=='__main__':
    run()
