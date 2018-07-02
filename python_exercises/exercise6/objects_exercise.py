# # Basics
# class Person: 
    
#     def __init__(self, name, email, phone): 
#         self.name = name 
#         self.email = email 
#         self.phone = phone

#     def greet(self, other_person): 
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny.greet(jordan)
# jordan.greet(sonny)

# print("Name: {}, Email: {}, Phone: {}".format(sonny.name, sonny.email, sonny.phone))

# print("Name: {}, Email: {}, Phone: {}".format(jordan.name, jordan.email, jordan.phone))


# # Make your own class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print("{} {} {}".format(self.year, self.make, self.model))
    

class Person: 
    
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone
        self.friends = []
        self.greeted = []
        self.greeting_count = 0

    def __str__(self):
        return "Name: {}, Email: {}, Phone: {}, Friends: {}, Greetings: {}".format(self.name, self.email, self.phone, self.friends, self.greeting_count)

    def print_contact_info(self):
        print("Name: {}, Email: {}, Phone: {}".format(self.name, self.email, self.phone))

    def add_friend(self, friend):
        self.friends.append(friend.name)

    def num_friends(self):
        print(len(self.friends))

    def greet(self, friend):
        print("Hello {}, I am {}.".format(friend.name, self.name))
        self.greeted.append(friend.name)
        self.greeting_count += 1

    def num_unique_people_greeted(self):
        uniquePeople = []

        for people in self.greeted:
            if people not in uniquePeople:
                uniquePeople.append(people)
        
        print("You greeted {} different people!".format(len(uniquePeople)))        

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(jordan)

jordan.num_unique_people_greeted()