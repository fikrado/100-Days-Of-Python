import pandas as pd

pd.read_csv("nato_phonetic_alphabet.csv")

dic_ph = {row.letter: row.code for (index, row) in data.iterrows()}
word = input(("enter word: ")).upper()
output = [dic_ph[l] for l in word]