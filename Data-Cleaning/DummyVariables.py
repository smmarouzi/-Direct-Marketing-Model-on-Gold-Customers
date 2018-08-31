# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:45:05 2018

@author: mm
"""

#read csv saved data
customers=pd.read_csv('customerssample.csv')
customers=customers.drop(['Unnamed: 0'],axis=1)
coupon=pd.read_csv('couponsample.csv')
coupon=coupon.drop(['Unnamed: 0'],axis=1)
service=pd.read_csv('servicesample.csv')
service=service.drop(['Unnamed: 0'],axis=1)
target=pd.read_csv('targetsample.csv')
target=target.drop(['Unnamed: 0'],axis=1)
spend=pd.read_csv('spendsample.csv')
spend=spend.drop(['Unnamed: 0'],axis=1)
demo_real=pd.read_csv('demo_realsample.csv')
demo_real=demo_real.drop(['Unnamed: 0'],axis=1)

## create dummy variables for object variables:
# dummy for customers
customers.set_index(['id'],inplace=True)
customers['internet_day'] = pd.to_datetime(customers['internet_day'])
customers['reg_day'] = pd.to_datetime(customers['reg_day'])
customers['birth'] = pd.to_datetime(customers['birth'])
dummy_cols=customers.select_dtypes(include=['object']).columns.tolist() # object variables
dummy_cols.remove('postcode')

dummy_table=pd.DataFrame(index=customers.index) # Dummy table initialization
for i in dummy_cols:
    dummy=pd.get_dummies(customers.loc[:,i],prefix=i)
    dummy_table=dummy_table.merge(dummy, how='inner', left_index=True, right_index=True)
customers.drop(dummy_cols,axis=1,inplace=True)
customers=customers.merge(dummy_table, how='inner', left_index=True, right_index=True)