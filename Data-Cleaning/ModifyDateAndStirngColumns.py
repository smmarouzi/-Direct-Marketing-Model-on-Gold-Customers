# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:47:44 2018

@author: mm
"""

# modify date and string columns in data tables
# date columns       
customerssample.dtypes
customerssample['internet_day']=pd.to_timedelta(customerssample['internet_day'], unit='D') + pd.Timestamp('1960-1-1')
customerssample['birth']=pd.to_timedelta(customerssample['birth'], unit='D') + pd.Timestamp('1960-1-1')

targetsample.dtypes

servicesample.dtypes
servicesample['service_day']=pd.to_timedelta(servicesample['service_day'], unit='D') + pd.Timestamp('1960-1-1')

spendsample.dtypes
spendsample['spend_day']=pd.to_timedelta(spendsample['spend_day'], unit='D') + pd.Timestamp('1960-1-1')

couponsample.dtypes
couponsample['coupon_day']=pd.to_timedelta(couponsample['coupon_day'], unit='D') + pd.Timestamp('1960-1-1')
#customers['internet_day']=pd.to_datetime(customers.internet_day,format='%d%b%Y')
customerssample.postcode.head()
# string columns
def modifyobjects(df):
    objectdf = df.select_dtypes(include=['object'])
    for col in objectdf.columns:
        df[col] = objectdf[col].str.decode('utf-8')
    return(df)
customerssample=modifyobjects(customerssample)        
spendsample=modifyobjects(spendsample)  
demo_realsample=modifyobjects(demo_realsample)

# save sample data
customerssample.to_csv('customerssample.csv')
couponsample.to_csv('couponsample.csv')
servicesample.to_csv('servicesample.csv')
targetsample.to_csv('targetsample.csv')
spendsample.to_csv('spendsample.csv')
demo_realsample.to_csv('demo_realsample.csv')