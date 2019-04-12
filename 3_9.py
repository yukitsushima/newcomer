#2019/04/11
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp
#For Python 2.7

from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score, matthews_corrcoef, roc_auc_score

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
