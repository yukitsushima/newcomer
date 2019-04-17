#2019/04/16
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score, matthews_corrcoef, roc_auc_score
from load_ionosphere import load_ionosphere
from sklearn.model_selection import *

#Help https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
#Help https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

[target, parameters] = load_ionosphere()
param_grid = {'C':[0.001, 0.01, 0.1, 1, 10, 100, 1000], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100, 1000]}
print('Evaluate with AUROC')
search_auroc = GridSearchCV(estimator=SVC(), param_grid=param_grid, scoring='roc_auc',cv=10, iid=False).fit(parameters, target)
print(search_auroc.best_params_)
print(search_auroc.best_score_)
print('Evaluate with F-score')
search_f = GridSearchCV(estimator=SVC(), param_grid=param_grid, scoring='f1',cv=10, iid=False).fit(parameters, target)
print(search_f.best_params_)
print(search_f.best_score_)
