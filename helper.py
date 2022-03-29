import sys

## write out text to file
## filename str
## text str
def text_to_new_file(filename, text):
    f_out = open(filename, "w")
    f_out.write(text)
    f_out.close()


def text_to_file(filename, text):
    f_out = open(filename, "a")
    f_out.write(text)
    f_out.close()


## reverse string
## text str
def string_reverse(text):
    return text[::-1]


## return 1 command line arg as str
def cline_str():
    return sys.argv

def GC_counter(seq):
    count = 0 
    for base in seq:
        if base == "G" or base == "C":
            count = count + 1
    return count

def baseCounter(seq):
    count = 0 
    for base in seq:
        if base == "G" or base == "C" or base == "A" or base == "T" or base == "U":
            count = count + 1
    return count

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line
