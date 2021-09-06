#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    list_of_names = file.readlines()

#Generate a list of names where each line of invited_names is an entry in the list
for _ in range(len(list_of_names)):
    list_of_names[_] = list_of_names[_].strip("\n")  # strip the \n line breaks from our names


for name in list_of_names:
    # we read the starting_letter and replace [name] with the name from our list
    with open("Input/Letters/starting_letter.txt") as file:
        file_text = file.read()
        new_text = file_text.replace("[name]", name)
    # take the stored new_text with the proper name in a new file called {name}.txt
    with open(f"Output/ReadyToSend/{name}.txt", "w") as output:
        output.write(new_text)
