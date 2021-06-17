DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
# Contante datos es una lista de diccionarios con datos de empleados 

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_python_devs2 = list(filter(lambda worker2: worker2["language"] == "python",DATA))
    all_python_devs2 = list(map(lambda worker2: worker2["name"], all_python_devs2))

    all_platzi_workers = [worker["name"] for worker in DATA if worker ["organization"] == "Platzi"]

    #si age es > 18 lambda = true y se almacena en lista 
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    # | pipe suma diccionarios fincion de python 3.9+
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in all_python_devs:
        print(worker)

    for worker2 in all_python_devs2:
        print(worker2)


if __name__=='__main__':
    run() 