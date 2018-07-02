# Define Functions
def set_an_entry():
    name = input("Please enter your name: ")
    number = input("Please enter your telephone number: ")

    contacts[name] = number

    print("Name: " + name)
    print("Phone Number: " + number)
    print("Entry stored for " + name + ".")

def look_up_an_entry():
    name = input("Name: ")
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

def list_all_entries():
    for key, values in contacts.items():
        print("Name: " + key + "; Number: " + values)

def userQuit():
    print("Bye.")


# Initialize Variables
playCheck = True
contacts = {}
print("Check")

# Phonebook Application
while playCheck:

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

    # Identify Function to Call Based on User Input
    if userInput == "1":
        look_up_an_entry()
    elif userInput == "2":
        set_an_entry()
    elif userInput == "3":
        delete_an_entry()
    elif userInput == "4":
        list_all_entries()
    elif userInput == "5":
        playCheck = False
        userQuit()
    else:
        print("Invalid entry, please try again.")
