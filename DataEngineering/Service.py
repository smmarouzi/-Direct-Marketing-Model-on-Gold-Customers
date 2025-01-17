# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:48:00 2018

@author: mm
"""

service=pd.read_csv('service.csv')
service=service.drop(['Unnamed: 0'],axis=1)

service.dtypes
service['service_day'] = pd.to_datetime(service['service_day'])

###
# data engineering:
time=[1,2,3,6] #1Month, 2Month, 3Month, 6Month
sta=['count']
trans=['log','sqrt']

## find days before last day for each transaction
n=service.groupby('id')['id'].count() # count each id
last_time=service.groupby('id')['service_day'].max() # find maximum date
# create the column of last date in spend dataframe
last_time_list=np.repeat(last_time,n)
service=service.set_index(['id']) 
service['last_time']=last_time_list
service.reset_index(level=0, inplace=True)
# find the diffrence between each date and last day
##spend['last_time']-relativedelta(months=+6)
service['days']=[(service['last_time'].iloc[i]-service['service_day'].iloc[i]).days for i in range(len(service))]

# Do data engineering for spend:
service2=pd.DataFrame()
'''
for i in trans:
    spend[i]=[eval('np.'+str(i)+'('+str(x)+')') for x in spend['spend']]
'''
for j in time:
    service_time = service.drop(service[service.days > j*30].index)
    for l in sta:
        service2['service_'+str(j)+'m_'+str(l)]=eval("service_time.groupby('id')['service_count']."+str(l)+"()")

service2.to_csv("service2.csv")     