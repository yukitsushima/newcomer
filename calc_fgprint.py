#2019/04/15
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

from rdkit import Chem
from rdkit.Chem import AllChem

def calc_fgprint(mol):
    return AllChem.GetMorganFingerprint(mol, 2)
