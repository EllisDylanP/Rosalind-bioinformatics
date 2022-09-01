oldbase = "T"
newbase = "U"

with open("C:\\Users\\dylan\\Downloads\\rosalind_rna (2).txt", "r") as A:
    A = A.read()
    C= A.replace(oldbase, newbase)
with open("C:\\Users\\dylan\\Downloads\\rosalind_rna (2).txt", "w") as B:
    B = B.write(C)

print(B)