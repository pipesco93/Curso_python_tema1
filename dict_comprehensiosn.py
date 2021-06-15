def run():
    # my_dict = {}

    # for i in range(1, 101): #Crear dict i = llaves i**3 valores
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

# hacer lo que esta cometado pero con dictionary comprehensiosns

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)


if __name__=='__main__':
    run()
