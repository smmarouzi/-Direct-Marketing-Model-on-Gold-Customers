# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:49:50 2018

@author: mm
"""

# Read model table
model_table=pd.read_csv('model_table.csv',index_col=['id']) 
  
# Correlation between target and variables:
corr_table=pd.DataFrame([1,1],index=['Pearson','spearman'],columns=['gold'])# Correlation table initial value
num_col=model_table.shape[1] # number of columns

omited_var=list()# list of variables which do not attend in correlation

for i in range(1,num_col):
    try:
        df=pd.DataFrame({'gold':model_table['gold'],model_table.columns[i]:model_table[model_table.columns[i]]})
        corr=pd.DataFrame([df.corr(method='pearson')['gold'][model_table.columns[i]],df.corr(method='spearman')['gold'][model_table.columns[i]]],
                  index=['Pearson','spearman'],columns=[model_table.columns[i]])
        corr_table=corr_table.merge(corr, how='inner', left_index=True, right_index=True)
    except:
        omited_var.append(model_table.columns[i])
        pass

corr_table=corr_table.dropna(axis=1, how='all') #drop nan values
# Save correlation table    
corr_table.to_csv('corr_table.csv')