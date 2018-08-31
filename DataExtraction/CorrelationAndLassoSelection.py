# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:50:06 2018

@author: mm
"""

from sklearn.linear_model import Lasso
#read correlation table and model table
corr_table=pd.read_csv('corr_table.csv',index_col=['Unnamed: 0'])
model_table=pd.read_csv('model_table.csv',index_col=['id'])

#select 100 higher correlations
corr_table=corr_table.abs()
max_100_corr=corr_table.max()
max_100_corr.sort_values(ascending=False,inplace=True)
max_100_corr=max_100_corr[:251]
# extract 100 features in model_table
last_100_cols=max_100_corr.index.tolist()
model_table_100=model_table[last_100_cols] # model_table with 100 variables
#fill Nan values with zero
model_table_100.fillna(0, inplace=True)
##model_table_100[model_table_100==float('-inf')]=0
#model_table_100=model_table_100[(model_table_100.T == float('-inf')).any()]
#
## remove rows zero
#model_table_100=model_table_100[(model_table_100.T != 0).any()]
#apply lasso 
names=model_table_100.drop(['gold'],axis=1).columns.tolist()

lasso = Lasso(alpha=.017)
lasso.fit(model_table_100.drop(['gold'],axis=1), model_table_100['gold'])
ranks = pd.Series(np.abs(lasso.coef_),index=names,name='Lasso_Coef') # Serie of each variable with lasso.coefficient

# find 25 biggest ranks values
ranks.sort_values(ascending=False,inplace=True)
ranks_25=ranks[:25]
last_25_cols=ranks_25.index.tolist()
last_25_cols.append('gold')
model_table_25=model_table_100[last_25_cols]
model_table_25.columns.tolist()
#ranks_25=pd.DataFrame(ranks_25,columns=['lasso_coefficient'])
#ranks_25.to_csv('rank_25.csv')
#save model_table_25
model_table_25.to_csv('model_table_25.csv')
# pairwise correlation for rank_25
#model_table_25_corr=model_table_25.corr(method='pearson')
#
## find features with high pairwise correlation
#for i in range(model_table_25_corr.shape[0]):
#    for j in range(i,model_table_25_corr.shape[1]):
#        model_table_25_corr.iloc[i,j]=0
#                                
#model_table_25_corr=model_table_25_corr.abs()
#pairwise_corr_value=model_table_25_corr.stack()
##find pairwise corr more than 0.75
#pairwise_corr_value=pairwise_corr_value[pairwise_corr_value>0.5]
#pairwise_corr_value.sort_values(ascending=False,inplace=True)
#pairwise_corr_value=pd.DataFrame(pairwise_corr_value,columns=['corr_value'])
#pairwise_corr_value.to_csv('pairwise_corr_value.csv')
#
#model_table_25=model_table[last_100_cols[75:]+['gold']]
#model_table_25.fillna(0, inplace=True)
k=0;
f=list()
last_25_cols.remove('gold')

for i in last_25_cols:
    p=last_25_cols.pop(k)
    f.append(p)
    k+=1
    print(i)
    for j in last_25_cols:
        corr_value=model_table_25.corr(method='pearson')[i][j]
        if abs(corr_value)>0.5:
            last_25_cols.remove(j)
            print(j)      
        
       
names=f+last_25_cols+['gold']
model_table_25=model_table_25[names]
  
model_table_25.to_csv('model_table_25.csv')   