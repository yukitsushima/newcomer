#2019/04/12
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D
#from IPython.display import SVG

suppl = Chem.SDMolSupplier('./testdata.sdf')
mols = [x for x in suppl if x is not None]
Draw.MolToImage(mols[8])
