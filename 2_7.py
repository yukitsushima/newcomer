path = './1BUW.pdb'
file = open(path)
lines = file.readlines()
WEIGHT =\
{ 'H':1.008,\
 'LI':6.941, 'BE':9.012,  'B':10.81,  'C':12.01,  'N':14.01,  'O':16.00,  'F':19.00,\
 'NA':22.99, 'MG':24.31, 'AL':26.98, 'SI':28.09,  'P':30.97,  'S':32.07, 'CL':35.45,}
total_weight = 0
x_weight = 0
y_weight = 0
z_weight = 0
for line in lines:
    if line[0:6] == 'ATOM  ':
        atom_number = int(line[6:11])
        atom_name = line[12:16].strip()
        identifier = line[16].strip()
        res_name = line[17:20].strip()
        chain = line[21].strip()
        res_number = int(line[22:26])
        res_code = line[26].strip()
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        occupy = float(line[54:60])
        tmp = line[60:66].strip()
        elem_symbol = line[76:78].strip()
        charge = line[78:80].strip()
        total_weight = total_weight + WEIGHT[elem_symbol]
        x_weight = x_weight + x * WEIGHT[elem_symbol]
        y_weight = y_weight + y * WEIGHT[elem_symbol]
        z_weight = z_weight + z * WEIGHT[elem_symbol]
print(str(total_weight))
print(str(x_weight/total_weight))
print(str(y_weight/total_weight))
print(str(z_weight/total_weight))
