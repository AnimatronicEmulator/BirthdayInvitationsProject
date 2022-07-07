# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as invited_names:
    names_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()

    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace('[name]', stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as invitation:
            invitation.write(new_letter)
