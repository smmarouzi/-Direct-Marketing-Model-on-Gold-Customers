# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:48:43 2018

@author: mm
"""

# data engineering:
time=[1,2,3,6] #1Month, 2Month, 3Month, 6Month
sta=['min','max','mean','std','count']
trans=['log','sqrt']
tp=['g','s','o']

## find days before last day for each transaction
n=spend.groupby('id')['id'].count() # count each id
last_time=spend.groupby('id')['spend_day'].max() # find maximum date
# create the column of last date in spend dataframe
last_time_list=np.repeat(last_time,n)
spend=spend.set_index(['id']) 
spend['last_time']=last_time_list
spend.reset_index(level=0, inplace=True)
# find the diffrence between each date and last day
##spend['last_time']-relativedelta(months=+6)
spend['days']=[(spend['last_time'].iloc[i]-spend['spend_day'].iloc[i]).days for i in range(len(spend))]

# Do data engineering for spend:
spend2=pd.DataFrame()
#spend[spend['spend']<0]=0
for i in trans:
    spend['spend_'+str(i)]=[eval('np.'+str(i)+'('+str(x)+')') for x in spend['spend']]
for j in time:
    spend_time = spend.drop(spend[spend.days > j*30].index)
    for k in tp:
        for l in sta:
            spend2['spend_'+str(j)+'m_'+str(k)+'_'+str(l)]=eval("spend_time[spend_time['spend_type']=='"+str(k)+"'].groupby('id')['spend']."+str(l)+"()")
            spend2['spend_'+str(j)+'m_all_'+str(l)]=eval("spend_time.groupby('id')['spend']."+str(l)+"()")
            for i in trans:
                spend2['spend_'+str(j)+'m_'+str(k)+'_'+str(l)+'_'+str(i)]=eval("spend_time[spend_time['spend_type']=='"+str(k)+"'].groupby('id')['spend_"+str(i)+"']."+str(l)+"()")
                spend2['spend_'+str(j)+'m_all_'+str(l)+'_'+str(i)]=eval("spend_time.groupby('id')['spend_"+str(i)+"']."+str(l)+"()")

spend2.to_csv("spend2.csv")               

#import sys
#sys.float_info.epsilon   
spend.drop(spend[spend['spend']<=0].index,inplace=True)