docs = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин', 'shelf': '1'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов', 'shelf': '2'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов', 'shelf': '3'}
]
shelves = ['1', '2', '3']
def get_owner(doc_num):
    for doc in docs:
        if doc['number'] == doc_num:
            return doc['name']
    return None


def get_shelf(doc_num):
    for doc in docs:
        if doc['number'] == doc_num:
            return doc['shelf']
    return None


def list_documents():
    print("Список всех документов:")
    for doc in docs:
        print(f"Тип: {doc['type']}, Номер: {doc['number']}, Владелец: {doc['name']}, Полка: {doc['shelf']}")


def add_shelf():
    new_shelf = input("Введите номер новой полки: ")
    if new_shelf in shelves:
        print("Полка с таким номером уже существует.")
    else:
        shelves.append(new_shelf)
        print(f"Полка {new_shelf} успешно добавлена.")


def delete_shelf():
    shelf_to_delete = input("Введите номер полки для удаления: ")

    if any(doc['shelf'] == shelf_to_delete for doc in docs):
        print("Невозможно удалить полку, так как она не пустая.")
    else:
        if shelf_to_delete in shelves:
            shelves.remove(shelf_to_delete)
            print(f"Полка {shelf_to_delete} успешно удалена.")
        else:
            print("Полка с таким номером не найдена.")


def main():
    while True:
        cmd = input(
            "Введите команду (p - узнать владельца, s - узнать полку, l - список документов, ads - добавить полку, ds - удалить полку, q - выход): ")

        if cmd == "q":
            print("Выход из программы.")
            break

        if cmd == "p":
            doc_num = input("Введите номер документа: ")
            owner = get_owner(doc_num)
            if owner:
                print("Владелец документа:", owner)
            else:
                print("Документ не найден.")

        elif cmd == "s":
            doc_num = input("Введите номер документа: ")
            shelf = get_shelf(doc_num)
            if shelf:
                print("Документ хранится на полке:", shelf)
            else:
                print("Документ не найден.")

        elif cmd == "l":
            list_documents()

        elif cmd == "ads":
            add_shelf()

        elif cmd == "ds":
            delete_shelf()


if __name__ == "__main__":
    main()
