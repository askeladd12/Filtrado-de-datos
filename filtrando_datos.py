DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Google',
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
        'name': 'Héctor',
        'age': 19,
        'organization': 'Facebook',
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
        'organization': 'Youtube',
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
def run():


    #Trabajadores que dominan python
    all_python_devs = [worker["name"] for worker in DATA if worker ["language"] == "python"] 


    #trabajadores de platzi
    all_platzi_workers = [worker["name"] for worker in DATA if worker ["organization"] == "Platzi"] 

    #Trabajadores que sean mayores de 18 años
    adults = list(filter(lambda worker: worker["age"] > 18 , DATA))

    #filtrado de la variable adults
    adults = list(map(lambda worker: worker["name"],adults))

    #devolver True a las personas mayores de 70 en un nuevo diccionario
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    print("trabajadores que dominan el leguaje python")
    for worker in all_python_devs:
        print(worker)
    
    print('*'*50)
    print("trabajadores de platzi")
    for worker in all_platzi_workers:
        print(worker)

    print('*'*50)
    print("trabajadores mayores de edad")
    for worker in adults:
        print(worker)

    print('*'*50)
    print("trabajadores mayores de 70 años")
    for worker in old_people:
        print(worker)

if __name__ == ('__main__'):
    run()
