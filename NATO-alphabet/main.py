import pandas as pd
df = pd.read_csv(r"NATO-alphabet\data\nato_phonetic_alphabet.csv")

# creating nato dictionary
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    inp = input("Enter a word: ").upper()
    try:
        lst  = [nato_dict[letter] for letter in inp]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else: 
        print(lst)
        
generate_phonetic()

# NOTE: Loop through rows of a data frame
# for (index, row) in df.iterrows():
    #Access index and row
    #Access row.student or row.score

# NOTE: Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
