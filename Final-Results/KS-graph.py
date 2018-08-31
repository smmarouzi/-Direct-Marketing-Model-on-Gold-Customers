# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:51:34 2018

@author: mm
"""

## KS chart
KS_table=pd.DataFrame(probability_df.groupby(['prob_cut_10'])['gold'].count())
KS_table.rename(columns={'gold':'N'},inplace=True)
KS_table['target_num']=probability_df.groupby(['prob_cut_10'])['gold'].sum()
KS_table.sort_values(['target_num'],ascending=False,inplace=True)
KS_table['non_target_num']=KS_table['N']-probability_df.groupby(['prob_cut_10'])['gold'].sum()
KS_table['within_target_rate'] = KS_table['target_num']/sum(KS_table['target_num'])
KS_table['within_non_target_rate'] = KS_table['non_target_num']/sum(KS_table['non_target_num'])
KS_table['within_target_cum_rate']=np.cumsum(KS_table['within_target_rate'])
KS_table['within_non_target_cum_rate']=np.cumsum(KS_table['within_non_target_rate'])
KS_table['K_S']=KS_table['within_target_cum_rate']-KS_table['within_non_target_cum_rate']
KS=KS_table['K_S'].max()
print(KS)

import matplotlib.pyplot as plt

plt.figure()
xs = np.arange(0, 10)
ys = KS_table['within_target_cum_rate']
plt.plot(xs,ys,color='darkorange',linewidth=2,label='%target' )
x2s = np.arange(0, 10)
y2s = KS_table['within_non_target_cum_rate']
plt.plot(x2s,y2s, color='navy',linewidth=2, label='%non_target')
#plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in gca().get_yticks()])
plt.xlim([-1, 11.0])
plt.ylim([0 , 1])
plt.xlabel('Deciles')
plt.ylabel('within_rate')
plt.title('KS chart (KS = '+str(round(KS*100))+'%)')
plt.legend(loc="lower right")
formatter = FuncFormatter(to_percent)
# Set the formatter
plt.gca().yaxis.set_major_formatter(formatter)
plt.show()
