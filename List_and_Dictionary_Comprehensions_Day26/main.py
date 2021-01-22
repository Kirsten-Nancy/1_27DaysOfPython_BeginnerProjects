import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_phonetic_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
# phonetic_code_list = [value for (key, value) in nato_phonetic_alphabet_dict.items() if key in user_input]
phonetic_code_list = [nato_phonetic_alphabet_dict[letter] for letter in user_input]
print(phonetic_code_list)