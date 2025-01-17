# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:53:49 2018

@author: mm
"""

# We have a table of 25 features
# After modeling and removing relutance or bad features we just have 8 features


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score  
from sklearn import metrics

model_table_25=pd.read_csv('model_table_25.csv',index_col=['id'])


X_train, X_test, y_train, y_test=train_test_split(model_table_25.drop(['gold'],axis=1),model_table_25.gold,test_size = 0.3)
clf = LogisticRegression(C=100).fit(X_train, y_train)
score=accuracy_score(y_test, clf.predict(X_test))
#preds = clf.predict(X_test)
probability=pd.Series(clf.predict_proba(X_test)[:,1],index=X_test.index,name='prob')
fpr, tpr, _ = metrics.roc_curve(y_test, clf.predict_proba(X_test)[:,1])
auc = metrics.auc(fpr,tpr)

remove_columns_names=model_table_25.drop(['gold'],axis=1).columns.tolist()[::-1]
for i in remove_columns_names:
    X_train.drop([i],axis=1)
    X_test.drop([i],axis=1)

    clf = LogisticRegression(C=100).fit(X_train, y_train)
    score=accuracy_score(y_test, clf.predict(X_test))
    #preds = clf.predict(X_test)
    fpr, tpr, _ = metrics.roc_curve(y_test, clf.predict_proba(X_test)[:,1])
    auc1 = metrics.auc(fpr,tpr)
    if auc<=auc1:
        X_train.drop([i],axis=1,inplace=True)
        X_test.drop([i],axis=1,inplace=True)
        model_table_25.drop([i],axis=1,inplace=True)
        print(i,round(auc1,4),round(auc,4))
        #k+=1
        auc=auc1
    
model_table_25.to_csv('model_table_8_final.csv')