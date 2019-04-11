#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys

#file open
args = sys.argv
if len(args) != 2:
    sys.stderr.write('Usage: python 1_1.py ./NT_113952.1.fasta\n')
    sys.exit()
path = args[1]
try:
    file = open(path)
except:
    sys.stderr.write('Error in opening file.\n')
    sys.exit()
lines = file.readlines()
length = len(lines)

#counter(num of A/T/G/C)
noA = 0
noT = 0
noG = 0
noC = 0
#Process with each line
#Skip Header
for l in range(1, length):
    noA = noA + lines[l].count('A')
    noT = noT + lines[l].count('T')
    noG = noG + lines[l].count('G')
    noC = noC + lines[l].count('C')
print("A:"+str(noA))
print("T:"+str(noT))
print("G:"+str(noG))
print("C:"+str(noC))
file.close()
