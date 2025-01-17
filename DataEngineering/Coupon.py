# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:48:58 2018

@author: mm
"""

coupon=pd.read_csv('coupon.csv')
coupon=coupon.drop(['Unnamed: 0'],axis=1)

coupon.dtypes
coupon['coupon_day'] = pd.to_datetime(coupon['coupon_day'])

###
# data engineering:
time=[1,2,3,6] #1Month, 2Month, 3Month, 6Month
sta=['min','max','mean','std','count']
trans=['log','sqrt']

## find days before last day for each transaction
n=coupon.groupby('id')['id'].count() # count each id
last_time=coupon.groupby('id')['coupon_day'].max() # find maximum date
# create the column of last date in spend dataframe
last_time_list=np.repeat(last_time,n)
coupon=coupon.set_index(['id']) 
coupon['last_time']=last_time_list
coupon.reset_index(level=0, inplace=True)
# find the diffrence between each date and last day
##spend['last_time']-relativedelta(months=+6)
coupon['days']=[(coupon['last_time'].iloc[i]-coupon['coupon_day'].iloc[i]).days for i in range(len(coupon))]

# Do data engineering for spend:
coupon2=pd.DataFrame()

for i in trans:
    coupon['amount_'+str(i)]=[eval('np.'+str(i)+'('+str(x)+')') for x in coupon['amount']]

for j in time:
    coupon_time = coupon.drop(coupon[coupon.days > j*30].index)
    for l in sta:
        coupon2['coupon_'+str(j)+'m_'+str(l)]=eval("coupon_time.groupby('id')['amount']."+str(l)+"()")
        for i in trans:
            coupon2['coupon_'+str(j)+'m_'+str(l)+'_'+str(i)]=eval("coupon_time.groupby('id')['amount_"+str(i)+"']."+str(l)+"()")

coupon2.fillna(0, inplace=True)
coupon2.to_csv("coupon2.csv")              