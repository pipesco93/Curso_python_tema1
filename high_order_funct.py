# Filter function
my_list = [1, 4, 5, 6, 9, 13,19, 21]
#Filter the list jus with odd numbers
#lambda recive x y retorna true si x%2 != 0
# al emvolver filter con list obtengo mi lista 
#filter devuelve un iterable
odd = list(filter(lambda x: x%2 != 0, my_list))

print(odd)
#-------------------------------------------------

#Map fun
my_list2 = [1, 2, 3, 4, 5]

# lambda recibe x y retorna x**2 y lo guarda en squares 
squares = list(map(lambda x: x**2, my_list2))

print(squares)

#-------------------------------------------------

# Reduce function

from functools import reduce

my_list3 = [2, 2, 2, 2, 2]

# lambda primer parámetro y lista segundo parámetro
# a * b = 4 --> 4 pasa a ser a y 4*2 = 8 y asi sigue
all_multiplied = reduce(lambda a, b: a * b, my_list3)

print(all_multiplied)
print(type(all_multiplied))