PLACEHOLDER = "[name]"

with open(r"Files, Directories & Paths\Input\Names\invited_names.txt") as file:
    # readlines() method returns a list of string in each line
    names = file.readlines()
    
with open(r"Files, Directories & Paths\Input\Letters\starting_letter.txt") as letter_file:
    # read() method returns the content in the file as a string
    content = letter_file.read()
    for name in names:
        # strip() mothod strips the string or sentence from excess spaces and newline
        name = name.strip()
        # replace() method replacces 1st param with 2nd param in a string
        new_letter = content.replace(PLACEHOLDER, name)
        with open(f"Files, Directories & Paths\Output\ReadyToSend\letter_for_{name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)
            