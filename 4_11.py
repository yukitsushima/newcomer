#2019/04/15
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D

#Print rdkit Version
#print('rdkit versions: {}'.format(rdBase.rdkitVersion))

suppl = Chem.SDMolSupplier('./ci6b00005_si_002.txt', removeHs=False) #Supplier
mols = [x for x in suppl if x is not None]
Chem.Draw.MolToFile(mols[1], 'hoge.png', size=(500,500))
print(len(mols))
