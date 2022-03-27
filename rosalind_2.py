#!/usr/bin/env python3

##Transcribing DNA into RNA
## BlanchardMR - 3/27/2022
from helper import text_to_file

f_in = open("rosalind_rna.txt")
dna_string = f_in.read()

rna_copy = ""

for i in dna_string:
    if i == "A":
        rna_copy = rna_copy + "A"
    if i == "G":
        rna_copy = rna_copy + "G"
    if i == "T":
        rna_copy = rna_copy + "U"
    if i == "C":
        rna_copy = rna_copy + "C"

text_to_file("output.txt", rna_copy)
