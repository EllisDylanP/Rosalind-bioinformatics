a=open("C:\\Users\\dylan\\Downloads\\rosalind_dna.txt")

data = a.read()

countA = data.count("A")
countC = data.count("C")
countG = data.count("G")
countT = data.count("T")

print(countA,' ',countC, ' ',countG, ' ',countT)



