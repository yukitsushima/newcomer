#2019/04/18
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

import codecs
import csv
import sys
from calc_fgprint import calc_fgprint
from rdkit import rdBase, Chem

from sklearn import svm, model_selection, metrics
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

#Load Mols
suppl1 = Chem.SDMolSupplier('./dataset1.sdf', removeHs=False) #Supplier
suppl3 = Chem.SDMolSupplier('./ci6b00005_si_002.txt', removeHs=False) #Supplier
suppl4 = Chem.SDMolSupplier('./dataset4.sdf', removeHs=False) #Supplier
suppl8 = Chem.SDMolSupplier('./dataset8.sdf', removeHs=False) #Supplier
mols = [x for x in suppl3 if x is not None]
mols_set3 = mols[106:210]
mols_set1 = [x for x in suppl1 if x is not None]
mols_set4 = [x for x in suppl4 if x is not None]
mols_set8 = [x for x in suppl8 if x is not None]
finger1 = []
finger3 = []
finger4 = []
finger8 = []
for data in mols_set1:
    finger1.append(calc_fgprint(data))
for data in mols_set3:
    finger3.append(calc_fgprint(data))
for data in mols_set4:
    finger4.append(calc_fgprint(data))
for data in mols_set8:
    finger8.append(calc_fgprint(data))

#Load RRCKs
csv1 = open('./dataset1.csv', 'r')
f1 = csv.reader(csv1)
RRCK_set1 = []
for row in f1:
    RRCK_set1.append(float(row[0]))
csv3 = open('./dataset3.csv', 'r')
f3 = csv.reader(csv3)
RRCK_set3 = []
for row in f3:
    RRCK_set3.append(float(row[0]))
csv4 = open('./dataset4.csv', 'r')
f4 = csv.reader(csv4)
RRCK_set4 = []
for row in f4:
    RRCK_set4.append(float(row[0]))
csv8 = open('./dataset8.csv', 'r')
f8 = csv.reader(csv8)
RRCK_set8 = []
for row in f8:
    RRCK_set8.append(float(row[0]))

#Learn
svr = SVR(kernel='rbf', C=100, gamma=0.01).fit(finger3, RRCK_set3)
def rmse(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))

#Predict and output
pre1 = svr.predict(finger1)
with codecs.open('predict1.csv', 'w', 'utf-8') as f:
    for i in range(0,len(pre1)):
        f.write(str(RRCK_set1[i])+','+str(pre1[i])+'\n')
print("Dataset 1")
print('R2_score : {}'.format(r2_score(RRCK_set1, pre1)))
print('RMSE : {}'.format(rmse(RRCK_set1, pre1)))
pre3 = svr.predict(finger3)
with codecs.open('predict3.csv', 'w', 'utf-8') as f:
    for i in range(0,len(pre3)):
        f.write(str(RRCK_set3[i])+','+str(pre3[i])+'\n')
print("Dataset 3")
print('R2_score : {}'.format(r2_score(RRCK_set3, pre3)))
print('RMSE : {}'.format(rmse(RRCK_set3, pre3)))
pre4 = svr.predict(finger4)
with codecs.open('predict4.csv', 'w', 'utf-8') as f:
    for i in range(0,len(pre4)):
        f.write(str(RRCK_set4[i])+','+str(pre4[i])+'\n')
print("Dataset 4")
print('R2_score : {}'.format(r2_score(RRCK_set4, pre4)))
print('RMSE : {}'.format(rmse(RRCK_set4, pre4)))
pre8 = svr.predict(finger8)
with codecs.open('predict8.csv', 'w', 'utf-8') as f:
    for i in range(0,len(pre8)):
        f.write(str(RRCK_set8[i])+','+str(pre8[i])+'\n')
print("Dataset 8")
print('R2_score : {}'.format(r2_score(RRCK_set8, pre8)))
print('RMSE : {}'.format(rmse(RRCK_set8, pre8)))
