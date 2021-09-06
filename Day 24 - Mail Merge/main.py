#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    list_of_names = file.readlines()

for _ in range(len(list_of_names)):
    list_of_names[_] = list_of_names[_].strip("\n")

print(list_of_names)

for name in list_of_names:
    with open("Input/Letters/starting_letter.txt") as file:
        