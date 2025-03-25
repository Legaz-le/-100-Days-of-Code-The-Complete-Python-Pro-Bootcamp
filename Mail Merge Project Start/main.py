#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
search_word = "[name]"

with open ("/Users/sdasa/Downloads/Mail Merge Project Start/Input/Names/invited_names.txt") as invited_names:
        names = invited_names.readlines()

with open ("/Users/sdasa/Downloads/Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    letter_content = starting_letter.read()

for name in names:
    striped_name = name.strip()
    new_letter = letter_content.replace(search_word,  striped_name)
    with open(f"/Users/sdasa/Downloads/Mail Merge Project Start/Output/ReadyToSend/letter_for_{striped_name}.docx", mode = "w") as completed_Letter:
        completed_Letter.write(new_letter)
