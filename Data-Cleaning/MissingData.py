# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:47:14 2018

@author: mm
"""

# modify missing datas
def control_miss(df):
    # df: the data frame we want to find missing datas, replace them with mean,
    # create missing indicator columns and drop columns with lots of missing...
    
    # in numeric columns of dataframe, missing data rate=N 
    # if N<5% then just fill NA values with mean of that column
    # if 5%<N<30% then replace NA values with mean of that column and creat missing indicator
    # if 30%<N<80% then create missing indicator and drop that column
    # if 80%<N then just drop that column...
    
    # numericdf: the final modified data frame with missing rules
    
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    objectdf=df.select_dtypes(exclude=numerics)
    numericdf = df.select_dtypes(include=numerics)
    if 'id' in df.columns:
        numericdf=numericdf.drop(['id'],axis=1)
    miss_num=numericdf.isnull().sum().tolist()
    rownum=numericdf.shape[0]
    miss_per=[x/rownum for x in miss_num]
    
    for i in range(len(miss_per)):                 
        if miss_per[i]<0.05:
            numericdf.iloc[:,i]=numericdf.iloc[:,i].fillna(numericdf.iloc[:,i].mean())
        elif miss_per[i]<0.3:
            numericdf['ind_'+str(numericdf.columns[i])]=numericdf.iloc[:,i].isnull()*1
            numericdf.iloc[:,i]=numericdf.iloc[:,i].fillna(numericdf.iloc[:,i].mean())
        elif miss_per[i]<0.8:
            numericdf['ind_'+str(numericdf.columns[i])]=numericdf.iloc[:,i].isnull()*1
            numericdf.drop(numericdf.columns[i],axis=1,inplace=True)
        else:
            numericdf.drop(numericdf.columns[i],axis=1,inplace=True)
        if 'id' in df.columns:
            frames=[df.id.astype('int'),objectdf,numericdf]
        else:
            frames=[objectdf,numericdf]
        modifieddf=pd.concat(frames,axis=1)
    return (modifieddf)

# modify missing data in each table
customers=control_miss(customers)
coupon=control_miss(coupon)
service=control_miss(service)
demo_real=control_miss(demo_real)
spend=control_miss(spend)                                      

# save data
customers.to_csv('customers.csv')
coupon.to_csv('coupon.csv')
service.to_csv('service.csv')
target.to_csv('target.csv')
spend.to_csv('spend.csv')
demo_real.to_csv('demo_real.csv')                                      
explore.to_csv('explore.csv')