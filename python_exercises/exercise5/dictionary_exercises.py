# Exercise 1
phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])

phonebook_dict['Kareem'] = '938-489-1234'
del(phonebook_dict['Alice'])
phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict)


# Nested Dictionaries
ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])

# Letter Summary
def letter_histogram(word):
    histogram = {}

    for letter in word:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1

    print(histogram)
    
letter_histogram("banana")

# Word Summary
def word_histogram(sentence):
    histogram = {}
    word = ""

    for letter in sentence:
        if letter.isalpha():
            word += letter
        else:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
            
            word = ""
    
    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1
    
    print(histogram)

word_histogram("hey yo yo yo hey what is up dude dude")