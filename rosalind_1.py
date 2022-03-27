## BlanchardMR - 3/27/2022
## O(n) complexity

# sample data
dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

adnine = 0
thymine = 0
guanine = 0
cytosine = 0
total = 0

for i in dna_string:
    if i == "A":
        adnine = adnine + 1
    if i == "T":
        thymine = thymine + 1
    if i == "G":
        guanine = guanine + 1
    if i == "C":
        cytosine = cytosine + 1

total = adnine + thymine + guanine + cytosine

print("DNA String is %dbp" % (len(dna_string)))

print(
    "adnine = %s, thymine = %s, guanine = %s cytosine = %s"
    % (
        adnine,
        thymine,
        guanine,
        cytosine,
    )
)

print("total counted %dbp" % (total))
