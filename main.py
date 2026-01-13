from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Некоректний номер телефону")
        else:
            self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        self.phones.append(Phone(value))

    def remove_phone(self, phone_str):
        for p in self.phones:
            if p.value == phone_str:
                self.phones.remove(p)
                break

    def find_phone(self, phone_str):
        for p in self.phones:
            if p.value == phone_str:
                return p
        else:
            return None
        
    def edit_phone(self, old_phone, new_phone):
        found = self.find_phone(old_phone)
        if found is None:
            raise ValueError("Такого телефону немає.")
        else:
            self.phones.remove(found)
            self.phones.append(Phone(new_phone))

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, find_name):
        record = self.data.get(find_name)
        return record

    def delete(self, delete_name):
        if delete_name in self.data:
            del self.data[delete_name]


if __name__ == "__main__":
        # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")