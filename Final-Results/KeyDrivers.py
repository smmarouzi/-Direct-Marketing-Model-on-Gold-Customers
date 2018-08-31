# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:52:16 2018

@author: mm
"""

#.............plot key_drivers
for cols in model_table_8.drop(['gold'],axis=1).columns:
    plt.figure()
    x = np.arange(10)
    plt.bar(x, decile_table[cols])
    plt.xlim([-1, 10])
    plt.xlabel('Deciles')
    plt.ylabel(str(cols))
    plt.title('key driver: '+str(cols))
    plt.show() 


#### ..............................................    
# key driver importance level:
std=list()
for cols in model_table_8.drop(['gold'],axis=1).columns:
    X_train2=pd.DataFrame(X_train[cols])
    X_test2=pd.DataFrame(X_test[cols])
    clf = LogisticRegression(C=100).fit(X_train2/ np.std(X_train2, 0), y_train)
    std.append(float(clf.coef_))

STDestimate=pd.DataFrame({'std':np.abs(std)},index=model_table_8.drop(['gold'],axis=1).columns.tolist())
STDestimate.sort_values(['std'],ascending=False,inplace=True)

# Plot importance level of key drivers:
#import pylab as pl
plt.figure()
STDestimate.plot(kind="bar", legend=False)
plt.xlabel('Key drivers')
plt.ylabel('STD estimation')
plt.title('Importance level of key drivers')
plt.show() 

plt.figure()
x = STDestimate.index.tolist()
y_pos = np.arange(len(x))
plt.bar(y_pos, STDestimate['std'], align='center', alpha=0.5)
plt.xticks(y_pos, x)
plt.xlim([-1, 8])
plt.ylim([0 , 3])
