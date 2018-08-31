# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:53:06 2018

@author: mm
"""

# statistical characteristics:            
import statsmodels.api as sm
logit = sm.Logit(y_train, X_train)  
result=logit.fit()
print(result.summary())                  
print(result.conf_int())        