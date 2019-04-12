#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import math
import sys

#file open
args = sys.argv
if len(args) != 3:
    sys.stderr.write('Usage: python 2_7.py ./1BUW.pdb A\n')
    sys.exit()
path = args[1]
try:
    file = open(path)
except:
    sys.stderr.write('Error in opening file.\n')
    sys.exit()
lines = file.readlines()

WEIGHT =\
{ 'H':1.008,\
 'LI':6.941, 'BE':9.012,  'B':10.81,  'C':12.01,  'N':14.01,  'O':16.00,  'F':19.00,\
 'NA':22.99, 'MG':24.31, 'AL':26.98, 'SI':28.09,  'P':30.97,  'S':32.07, 'CL':35.45,}
total_weight = 0
x_weight = 0
y_weight = 0
z_weight = 0
atom_data = []
for line in lines:
    if line[0:6] == 'ATOM  ' and line[21] == args[2]:
        #Parse Data
        atom_number = int(line[6:11])
        atom_name = line[12:16].strip()
        #identifier = line[16].strip()
        #res_name = line[17:20].strip()
        #chain = line[21].strip()
        #res_number = int(line[22:26])
        #res_code = line[26].strip()
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        #occupy = float(line[54:60])
        #tmp = line[60:66].strip()
        elem_symbol = line[76:78].strip()
        #charge = line[78:80].strip()

        #Calculate Center of Grabity
        total_weight = total_weight + WEIGHT[elem_symbol]
        x_weight = x_weight + x * WEIGHT[elem_symbol]
        y_weight = y_weight + y * WEIGHT[elem_symbol]
        z_weight = z_weight + z * WEIGHT[elem_symbol]

        #Register Atom Data
        atom_data.append([x, y, z, atom_number, atom_name, elem_symbol])
#IF no Data
if total_weight == 0:
    sys.stderr.write('Chain '+args[2]+' does not exist.\n')
    sys.exit()

#Calculate Center of Grabity
x_balance = x_weight / total_weight
y_balance = y_weight / total_weight
z_balance = z_weight / total_weight

#Calculate circle r
r = 0
for data in atom_data:
    r = r + math.sqrt((data[0]-x_balance)**2+(data[1]-y_balance)**2+(data[2]-z_balance)**2)
r = r / len(atom_data)
print('Center: ('+str(x_balance)+', '+str(y_balance)+', '+str(z_balance)+')')
print('Radius: '+str(r))

file.close()
