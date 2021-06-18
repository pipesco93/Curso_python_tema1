def divisor(num):
    divisor =[]
    for i in range(1, num+1):
        if num % i == 0:
            divisor.append(i)
    return(divisor)

def run():
    while True:
        try:
            num = int(input("Ingres un número: "))
            if num < 0:
                print("Debes ingresar un número positivo")
                continue
            print(divisor(num))
            break
        except ValueError:
            print("Debes ingresar un número")


if __name__=='__main__':
    run()