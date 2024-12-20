from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Field for storing contact name (mandatory)."""
    pass

class Phone(Field):
    """Field for storing and validating phone numbers."""

    def __init__(self, value):
        self._validate(value)
        super().__init__(value)

    @staticmethod
    def _validate(value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")

class Record:
    """Stores a contact's name and their associated phone numbers."""

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if ph.value == old_phone:
                self.phones.remove(ph)
                self.add_phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """Manages and stores multiple contact records."""

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Testing the implementation
if __name__ == "__main__":
    # Create an AddressBook instance
    book = AddressBook()

    # Add a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    # Add a record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Display all records
    for name, record in book.items():
        print(record)

    # Edit a phone number for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

    # Find a specific phone number for John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Delete a record for Jane
    book.delete("Jane")
    print("After deletion:")
    for name, record in book.items():
        print(record)
