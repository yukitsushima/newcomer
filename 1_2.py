#2019/04/05
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys
from rev import rev
from combine import combine

#file open
args = sys.argv
if len(args) != 2:
    sys.stderr.write('Usage: python 1_2.py ./NT_113952.1.fasta\n')
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
#Reverse
reverse = rev(text)
print(reverse)

file.close()
