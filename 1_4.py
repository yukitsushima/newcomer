#2019/04/08
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

from combine import combine
from rev import rev
from findall import findall

#file path
path = './NT_113952.1.fasta'
file = open(path).readlines()
file.pop(0)
text = combine(file)
reverse = rev(text)
index1 = findall(text, 'GAATTC')
index2 = findall(reverse, 'GAATTC')
index3 = findall(text, 'ATG')
index4 = findall(reverse, 'ATG')
print('GAATTC in STRING is berow:')
print(index1)
print('GAATTC in REVERSE STRING is berow:')
print(index2)
print('ATG in STRING is berow:')
print(index3)
print('ATG in REVERSE STRING is berow:')
print(index4)
