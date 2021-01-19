# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Readlines returns a list of file lines
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()

with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines()

for name in names:
    # To prevent the comma from going to next line
    new_name = name.strip('\n')
    path = f'./Output/ReadyToSend/letter_for_{new_name}.txt'
    with open(path, mode='w') as file:
        final_letter = letter_contents.replace('[name]', new_name)
        file.write(final_letter)

    # Use file.read which will return a string and replace that one string appropriately
    # thus only using one write function
    # with open(path, mode='w') as final_file:
    #     first_line = letter_contents[0].replace('[name]', new_name)
    #     final_file.write(first_line)
    # with open(path, mode='a') as file:
    #     for line in letter_contents[1:]:
    #         file.write(line)
