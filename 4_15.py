#2019/04/18
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 3.7

#User rdkit-env

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

param_grid = {'C':[0.001, 0.01, 0.1, 1, 10, 100, 1000], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100, 1000]}
def rmse(y, y_pred):
    return np.sqrt(mean_squared_error(y, y_pred))
search = GridSearchCV(estimator=SVR(), param_grid=param_grid, scoring='neg_mean_squared_error',cv=10, iid=False).fit(fingerprint, RRCK_set3)
print('R2_score : {}'.format(r2_score(RRCK_set3, search.predict(fingerprint))))
print('RMSE : {}'.format(rmse(RRCK_set3, search.predict(fingerprint))))
print('best_params : {}'.format(search.best_params_))
