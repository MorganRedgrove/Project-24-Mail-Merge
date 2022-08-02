#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    names = names.read().splitlines()
    for name in names:
        with open("./Input/Letters/starting_letter.txt") as letter:
            new_letter = open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w+")
            letter_string = letter.read()
            new_letter_string = letter_string.replace("[name]", name)
            new_letter.write(new_letter_string)
            new_letter.close()

