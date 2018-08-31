# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:52:38 2018

@author: mm
"""

model_table_8=pd.read_csv('model_table_8.csv',index_col=['id'])

X_train, X_test, y_train, y_test=train_test_split(model_table_8.drop(['gold'],axis=1),model_table_8.gold,test_size = 0.3)
clf = LogisticRegression(C=100).fit(X_train, y_train)
score=accuracy_score(y_test, clf.predict(X_test))
#preds = clf.predict(X_test)
probability=pd.Series(clf.predict_proba(X_test)[:,1],index=X_test.index,name='prob')
fpr, tpr, _ = metrics.roc_curve(y_test, clf.predict_proba(X_test)[:,1])
auc = metrics.auc(fpr,tpr)

## Plot ROC 
import matplotlib.pyplot as plt
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area ='+str(round(auc*100))+'%)')
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()