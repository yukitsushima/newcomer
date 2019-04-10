#2019/04/05
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

from rev import rev
from combine import combine

#file path
path = './NT_113952.1.fasta'
file = open(path).readlines()
#Skip Header
file.pop(0)
text = combine(file)
reverse = rev(text)
print(reverse)
