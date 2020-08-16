# Guided Exploration No. 3
# mitchell lee
import random


# a list to store variables into
possible_names = []


# opens the rap names output file and assigns it to outputFile
outputFile = open('rap-names-output.txt', 'w')


# use the file rap names and assign it to data file for code below
with open('rap-names.txt', 'r') as dataFile:
    # for each name listed in the file rap-names.txt run the code below that amount of times
    for name in dataFile:
        # for each iteration append each name to the variable possible_names
        possible_names.append(name.rstrip())


# asks you how many rapper names you want created and stores it in the variable 'count'
count = int(input('How many rap names would you like to create? '))
# asks you how many parts the name should have and stores it in the variable 'parts'
parts = int(input('How many parts should the name contain? '))


# loops the code below however many times "count" was assigned
for i in range(count):
    # a list to store variables into
    name_parts = []
    # loops the code below however many times "parts" was assigned
    for j in range(parts):
        # puts a random name that is listed in possible_names into
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])


# the code is saying that in the file assigned turn the list into a string and in between the words seperate them with a space and then put it into the file
    outputFile.write(f"{' '.join(name_parts)}\n")
# display the rapper names to the user
    print(f"{' '.join(name_parts)}")


# end program and view your rapper name in the file
outputFile.close()
