def main():
    contacts = {"Bob": 111111, "David": 443322, "Helen": 564235}
    while True:
        command = input("1 - Add\n2 - Delete\n3 - Browse\n4 - Edit phone\nPlease, enter command ")
        if command == "1":
            name = input("Enter name")
            if contacts.get(name):
                print("Such name already exists")
                continue
            tel = int(input("Enter phone"))
            contacts[name] = tel
            print(contacts)
        elif command == "2":
            name = input("Enter name")
            if contacts.get(name):
                contacts.pop(name)
                print(f"Contact {name} deleted")
            else:
                print(f"Contact {name} not found")
        elif command == "3":
            for name, phone in contacts.items():
                print(f"{name} - {phone}")
        elif command == "4":
            name = input("Enter name")
            if contacts.get(name):
                contacts[name] = int(input("Enter phone"))
            else:
                print("Contact not found")
main()