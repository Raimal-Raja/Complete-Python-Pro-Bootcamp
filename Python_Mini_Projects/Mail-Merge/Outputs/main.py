PLACEHOLDER = "[name]"

with open('../Inputs/names.txt') as names_file:
    names = names_file.readlines()
    print(names)

with open("../Inputs/letter.docs") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        # print(new_letter)
        with open(f"../Outputs/letter_for_{stripped_name}.docs", mode='w') as final_letter:
            final_letter.write(new_letter)