#2019/04/15
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

from rdkit import Chem
from rdkit.Chem import AllChem

def calc_fgprint(mol):
    data = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits = 2048)
    set = []
    for i in range(0,2048):
        if data.GetBit(i):
            set.append(1)
        else:
            set.append(0)
    return set
