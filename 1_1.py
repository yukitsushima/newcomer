#2019/04/05
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

#file path
path = './NT_113952.1.fasta'
file = open(path).readlines()
length = len(file)

#counter(num of A/T/G/C)
noA = 0
noT = 0
noG = 0
noC = 0
#Process with each line
#Skip Header
for l in range(1, length):
    noA = noA + file[l].count('A')
    noT = noT + file[l].count('T')
    noG = noG + file[l].count('G')
    noC = noC + file[l].count('C')
print("A:"+str(noA))
print("T:"+str(noT))
print("G:"+str(noG))
print("C:"+str(noC))
