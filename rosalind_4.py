#!/usr/bin/env python3
## Computing GC Content
## BlanchardMR - 3/28/2022
## complexity O(n) with constant memory usage
## Does not load entire FASTA file into memory
from helper import baseCounter, cline_str, peek_line, text_to_file, GC_counter, baseCounter

file_name = cline_str()  ## go back and fix this before running

count_tot = 0
count_GC = 0
label = ""
sequence = ""
results = {}

with open(file_name, "r") as file_in:
    for line in iter(file_in.readline, ''):
        line = line.strip()
        if line.startswith(">"):
            label = line[1:]
        else:
            sequence = sequence + line
            if peek_line(file_in).startswith(">") == True or peek_line(file_in) == "":
                results[label] = str("{0:.6f}".format((GC_counter(sequence)/baseCounter(sequence))*100))
                sequence = ""

largest = max(results, key=results.get)
text_to_file("text.txt", largest + "\n" + results.get(largest) + "\n")

##
# What I learned: Better to use an iter instead of the built in for-in construct as it has
# more options like tell() and seek() which are removed from the for-in iterator
# #       
        