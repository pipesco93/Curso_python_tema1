import random
import os

def sel_word():
    words = []
    with open("./data.txt","r", encoding="utf-8") as f: #encoding que todo se le abien tildes y cosas asi
        for line in f:
            words.append(line)
    word = random.choice(words)
    return word




def run():
    selected_word = sel_word().upper().strip()
    selected_word_list = [letter for letter in selected_word]
    word_dash = ["_"] * len(selected_word)
    letter_index_dict = {}

    for idx, letter in enumerate(selected_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
         
    while True:
        os.system("cls") 
        print("¡Adivina la palabra!")
        for element in word_dash:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in selected_word_list:
            for idx in letter_index_dict[letter]:
                word_dash[idx] = letter
        
        if "_" not in word_dash:
            os.system("cls")
            print("¡Ganaste! La palabra era", selected_word)
            break


       
        

if __name__=='__main__':
    run()