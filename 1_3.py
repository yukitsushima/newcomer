#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys
from combine import combine

#file open
args = sys.argv
if len(args) != 4:
    sys.stderr.write('Usage: python 1_3.py ./NT_113952.1.fasta 1000 300\n')
    sys.exit()
path = args[1]
try:
    file = open(path)
except:
    sys.stderr.write('Error in opening file.\n')
    sys.exit()
lines = file.readlines()

#Skip Header
lines.pop(0)
text = combine(lines)
length = len(text)

try:
    w = int(args[2])
    s = int(args[3])
except ValueError as e:
    sys.stderr.write('Incorrect w or s in command line args\n')
    sys.exit()

GC = []
bottom = 0
while bottom < length:
    part = text[bottom:bottom+w]
    if len(part) == 0:
        break
    GC.append((part.count('C') + part.count('G'))/float(len(part)))
    bottom = bottom + s
#Export for gnuplot
for i in range(len(GC)):
    print(str(i*300)+' '+str(GC[i]))

file.close()
