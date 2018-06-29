# Phone Book

# Initialize Contact Dictionary
contacts = {}

print("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit 
""")

userInput = input("What do you want to do? ")

def set_an_entry():
    name = input("Please enter your name: ")
    number = input("Please enter your telephone number: ")

    contacts[name] = number

    print("Name: " + name)
    print("Phone Number: " + number)
    print("Entry stored for " + name + ".")

def look_up_an_entry(name):
    if contacts.get(name) == None:
        print("No entry was found for " + name + ".")
    else:
        print("Found entry for " + name + ": " + contacts[name])

def delete_an_entry():
    name = input("Please enter your the name you would like to delete: ")

    if contacts.get(name) == None:
        print("No entry was found for " + name + ".")
    else:
        print("Deleted entry for " + name + ".")
        del(contacts[name])
        print(contacts)

def list_all_entries():
    for key, values in contacts.items():
        print("Name: " + key + "; Number: " + values)

