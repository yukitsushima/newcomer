#2019/04/16
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

import sys
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score, matthews_corrcoef, roc_auc_score
from load_ionosphere import load_ionosphere
from sklearn.model_selection import *

#TP, TN : True
#FN : actually positive, but expected negative
#FP : actually negative, but expected positive
#Precision : TP / TP + FP
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score
#Recall    : TP / TP + FN
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score
#F-measure : 2 * Recall * Precision / Recall + Precision
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score
#MCC : Matthews Correlation Coefficient
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef
#AUROC :
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score

svc = SVC(C=1.0, kernel='rbf', gamma=0.2)
kf = KFold(n_splits=10, shuffle=True)
[target, parameters] = load_ionosphere()
counter = 0
print('Set\tPreci.\tRecall\tMCC\tAUROC\tF-score')
for train_index, test_index in kf.split(parameters, target):
    counter = counter + 1
    train_param  = []
    train_target = []
    test_param   = []
    test_target  = []
    for i in range(0,len(train_index)):
        train_param.append(parameters[train_index[i]])
        train_target.append(target[train_index[i]])
    for i in range(0,len(test_index)):
        test_param.append(parameters[test_index[i]])
        test_target.append(target[test_index[i]])
    sys.stdout.write(str(counter)+'\t')
    learn = svc.fit(train_param, train_target)
    print(str(precision_score(test_target, learn.predict(test_param)))[0:7]+'\t'\
         +str(recall_score(test_target, learn.predict(test_param)))[0:7]+'\t'\
         +str(matthews_corrcoef(test_target, learn.predict(test_param)))[0:7]+'\t'\
         +str(roc_auc_score(test_target, learn.predict(test_param)))[0:7]+'\t'\
         +str(f1_score(test_target, learn.predict(test_param)))[0:7])
