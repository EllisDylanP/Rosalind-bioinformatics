## read sequence and get a new string opened
reverse = open("C:\\Users\\dylan\\Downloads\\output.txt", "w")
with open("C:\\Users\\dylan\\Downloads\\rosalind_revc (5).txt", "r") as primary:
    data = primary.read()

## flipping the order of the original sequence
data_1 = data[::-1]
reverse.write(data_1)
reverse.close()

## read newest string and open the final output string
with open("C:\\Users\\dylan\\Downloads\\output.txt", "r") as old:
    olld = old.read()
new = open("C:\\Users\\dylan\\Downloads\\new.txt", "w")

## writing complement nucleotide
olld = str(olld)
def change(list):
    emptystr = ""
    for element in range(0, len(list)):
        if list[element] == "A":
            emptystr += "T"
        if list[element] == "T":
            emptystr += "A"
        if list[element] == "G":
            emptystr += "C"
        if list[element] == "C":
            emptystr += "G"
    return emptystr

## write the final output string
neww = change(olld)
new.write(neww)
new.close()
old.close()

## visualize output
print(olld)
print(neww)
