import pandas as pd
df = pd.read_csv(r"NATO-alphabet\data\nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# creating nato dictionary

inp = input("Enter a word: ").upper()

try:
    lst  = [nato_dict[letter] for letter in inp]
    
except KeyError:
    print("Sorry, only letters in the alphabet please.")
    
else: 
    print(lst)

# NOTE: Loop through rows of a data frame
# for (index, row) in df.iterrows():
    #Access index and row
    #Access row.student or row.score

# NOTE: Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
