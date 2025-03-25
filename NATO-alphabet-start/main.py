
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
file = pandas.read_csv("nato_phonetic_alphabet.csv")

new_format = {row.letter:row.code for (index, row) in file.iterrows()}
checking = True
while checking:
    try:
        name = input("Type your name").upper()
        lists = [new_format[letter] for letter in name]
        print(lists)
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        checking = False





