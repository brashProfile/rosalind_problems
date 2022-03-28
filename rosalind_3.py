#!/usr/bin/env python3
## Complementing a Strand of DNA
## BlanchardMR - 3/27/2022
## complexity O(n)
from helper import text_to_file, string_reverse

f_in = open("rosalind_revc.txt")
dna_string = f_in.read()
dna_string = string_reverse(dna_string)
reverse_compliment = ""

for i in dna_string:
    if i == "A":
        reverse_compliment = reverse_compliment + "T"
    if i == "G":
        reverse_compliment = reverse_compliment + "C"
    if i == "T":
        reverse_compliment = reverse_compliment + "A"
    if i == "C":
        reverse_compliment = reverse_compliment + "G"

print(reverse_compliment)
text_to_file("output.txt", reverse_compliment)
