#2019/04/05
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

from combine import combine

#file path
path = './NT_113952.1.fasta'
file = open(path).readlines()
#Skip Header
file.pop(0)
text = combine(file)
length = len(text)
w = 1000
s = 300
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