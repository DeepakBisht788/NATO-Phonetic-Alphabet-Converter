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
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict)
dict_1={row.letter:row.code for (index,row) in data.iterrows()}
#print(dict_1)

def call():
    word = input(f"enter_word= ").upper()
    try:
        RESULT=[(dict_1[i]) for i in word]
    except:
        print(f"Sorry,only letters in the alphabet please.")
        call()
    else:
        print(RESULT)

call()


