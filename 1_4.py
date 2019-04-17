#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys
from combine import combine
from rev import rev
from findall import findall

#file open
args = sys.argv
if len(args) != 3:
    sys.stderr.write('Usage: python 1_4.py ./NT_113952.1.fasta GAATTC\n')
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
index1 = findall(text, args[2])
index2 = findall(reverse, args[2])
print(args[2]+' in STRING is below:')
print(index1)
print(args[2]+' in REVERSE STRING is below:')
print(index2)
file.close()
