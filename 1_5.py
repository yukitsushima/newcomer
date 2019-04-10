#2019/04/08
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

from combine import combine
from rev import rev
from decode import decode

#file path
path = '/mnt/fs/ohue/newcomer/NT_113952.1.fasta'
file = open(path).readlines()
file.pop(0)
text = combine(file)
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
