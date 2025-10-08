documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def GetOwnerByID():
    print("Введите номер документа:")
    id = input()
    print("Результат:")
    for i in documents:
        if i['number'] == id:
            print(f"Владелец документа: {i['name']}")
            return
    print("Владелец документа: владелец не найден")

def GetDirectoryByID():
    print("Введите номер документа:")
    id = input()
    print("Результат:")
    for i in directories:
        for j in directories[i]:
            if j == id:
                print(f"Документ хранится на полке: {i}")
                return
    print("Документ не найден.")
if __name__ == '__main__':
    while True:
        print("Введите команду:")
        command = input()
        if command == 'p':
            GetOwnerByID()
        elif command == 's':
            GetDirectoryByID()
        else:
            print("Команда отсутствует")
        print("Выполнить еще команду [y|n]?")
        more=input()
        if more.lower() == 'n':
            break
