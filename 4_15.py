#2019/04/15
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

import csv
import sys
from calc_fgprint import calc_fgprint
from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import rdMolDraw2D

from sklearn import *
from sklearn.svm import SVR
from sklearn.model_selection import *

#Load Mols
suppl = Chem.SDMolSupplier('./ci6b00005_si_002.txt', removeHs=False) #Supplier
mols = [x for x in suppl if x is not None]
mols_set3 = mols[106:210]
fingerprint = []
for data in mols_set3:
    fingerprint.append(calc_fgprint(data))

#Load RRCKs
csv_file = open('./dataset3.csv', 'r')
f = csv.reader(csv_file)
RRCK_set3 = []
for row in f:
    RRCK_set3.append(float(row[0]))

svr = SVR(kernel='rbf', C=10, gamma=0.01)
"""
kf = KFold(n_splits=10, shuffle=True)
for train_index, test_index in kf.split(fingerprint, RRCK_set3):
    train_param  = []
    train_target = []
    test_param   = []
    test_target  = []
    for i in range(0,len(train_index)):
        train_param.append(fingerprint[train_index[i]])
        train_target.append(RRCK_set3[train_index[i]])
    for i in range(0,len(test_index)):
        test_param.append(fingerprint[test_index[i]])
        test_target.append(RRCK_set3[test_index[i]])
    score = svr.fit(train_param, train_target).score(test_param, test_target)
    print(score)
"""

score = cross_val_score(estimator=svr, X=fingerprint, y=RRCK_set3, cv=10, n_jobs=-1)
print(sum(score)/len(score))
#print(cross_validate(svr, fingerprint, RRCK_set3, cv=10)['test_score'])
