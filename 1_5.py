#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys
from combine import combine
from rev import rev
from decode import decode

#file open
args = sys.argv
if len(args) != 2:
    sys.stderr.write('Usage: python 1_5.py ./NT_113952.1.fasta\n')
    sys.exit()
path = args[1]
try:
    file = open(path)
except:
    sys.stderr.write('Error in opening file.\n')
    sys.exit()
lines = file.readlines()

lines.pop(0)
text = combine(lines)
reverse = rev(text)
print('PEPTIDE 1')
print(decode(text,0))
print('PEPTIDE 2')
print(decode(text,1))
print('PEPTIDE 3')
print(decode(text,2))
print('PEPTIDE 4')
print(decode(reverse,0))
print('PEPTIDE 5')
print(decode(reverse,1))
print('PEPTIDE 6')
print(decode(reverse,2))
file.close()
