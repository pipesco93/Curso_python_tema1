def read():
    numbers = []
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f: #encoding que todo se le abien tildes y cosas asi
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian", "Rocío"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        #con "w" Reescribe cada que se ejecuta con "a" =append agrega si cambio la lista no se sobreescribe
        for name in names:
            f.write(name)
            f.write("\n")




def run():
    write()


if __name__=='__main__':
    run()