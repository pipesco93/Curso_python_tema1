def palindrome(string):

    assert len(string) > 0, "No s epuede ingresar una cadena vacía"
    return string == string[::-1]

def run():
    
    print(palindrome(""))
   
    
if __name__=='__main__':
    run()
