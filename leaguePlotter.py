import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('mens_leagues_reduced.csv')

#seperate the dataframe into a data frame for each value of column 'tier'
prem = df[df['tier'] == 'Premier']
div1 = df[df['tier'] == 'North/South1']
div2 = df[df['tier'] == 'North/South2']
t1 = df[df['tier'] == 'Tier1']
t2 = df[df['tier'] == 'Tier2']
t3 = df[df['tier'] == 'Tier3']
t4 = df[df['tier'] == 'Tier4']
t5 = df[df['tier'] == 'Tier5']
t6 = df[df['tier'] == 'Tier6']

#divide each data frame from t1 to t6 into 7 dataframes by field 'section' from 1 to 7
t1_1 = t1[t1['section'] == '1']
t1_2 = t1[t1['section'] == '2']
t1_3 = t1[t1['section'] == '3']
t1_4 = t1[t1['section'] == '4']
t1_5 = t1[t1['section'] == '5']
t1_6 = t1[t1['section'] == '6']
t1_7 = t1[t1['section'] == '7']

t2_1 = t2[t2['section'] == '1']
t2_2 = t2[t2['section'] == '2']
t2_3 = t2[t2['section'] == '3']
t2_4 = t2[t2['section'] == '4']
t2_5 = t2[t2['section'] == '5']
t2_6 = t2[t2['section'] == '6']
t2_7 = t2[t2['section'] == '7']

t3_1 = t3[t3['section'] == '1']
t3_2 = t3[t3['section'] == '2']
t3_3 = t3[t3['section'] == '3']
t3_4 = t3[t3['section'] == '4']
t3_5 = t3[t3['section'] == '5']
t3_6 = t3[t3['section'] == '6']
t3_7 = t3[t3['section'] == '7']

t4_1 = t4[t4['section'] == '1']
t4_2 = t4[t4['section'] == '2']
t4_3 = t4[t4['section'] == '3']
t4_4 = t4[t4['section'] == '4']
t4_5 = t4[t4['section'] == '5']
t4_6 = t4[t4['section'] == '6']
t4_7 = t4[t4['section'] == '7']

t5_1 = t5[t5['section'] == '1']
t5_2 = t5[t5['section'] == '2']
t5_3 = t5[t5['section'] == '3']
t5_4 = t5[t5['section'] == '4']
t5_5 = t5[t5['section'] == '5']
t5_6 = t5[t5['section'] == '6']
t5_7 = t5[t5['section'] == '7']

t6_1 = t6[t6['section'] == '1']
t6_2 = t6[t6['section'] == '2']
t6_3 = t6[t6['section'] == '3']
t6_4 = t6[t6['section'] == '4']
t6_5 = t6[t6['section'] == '5']
t6_6 = t6[t6['section'] == '6']
t6_7 = t6[t6['section'] == '7']

#Tier 1

# plt.scatter(t1_1['Lon'], t1_1['Lat'], c='r', label='Tier1_1')
# plt.scatter(t1_2['Lon'], t1_2['Lat'], c='g', label='Tier1_2')
# plt.scatter(t1_3['Lon'], t1_3['Lat'], c='b', label='Tier1_3')
# plt.scatter(t1_4['Lon'], t1_4['Lat'], c='y', label='Tier1_4')
# plt.scatter(t1_5['Lon'], t1_5['Lat'], c='c', label='Tier1_5')
# plt.scatter(t1_6['Lon'], t1_6['Lat'], c='m', label='Tier1_6')
# plt.scatter(t1_7['Lon'], t1_7['Lat'], c='k', label='Tier1_7')

#Tier 2
# plt.scatter(t2_1['Lon'], t2_1['Lat'], c='r', label='Tier2_1')
# plt.scatter(t2_2['Lon'], t2_2['Lat'], c='g', label='Tier2_2')
# plt.scatter(t2_3['Lon'], t2_3['Lat'], c='b', label='Tier2_3')
# plt.scatter(t2_4['Lon'], t2_4['Lat'], c='y', label='Tier2_4')
# plt.scatter(t2_5['Lon'], t2_5['Lat'], c='c', label='Tier2_5')
# plt.scatter(t2_6['Lon'], t2_6['Lat'], c='m', label='Tier2_6')
# plt.scatter(t2_7['Lon'], t2_7['Lat'], c='k', label='Tier2_7')

#Tier 3
# plt.scatter(t3_1['Lon'], t3_1['Lat'], c='r', label='Tier3_1')
# plt.scatter(t3_2['Lon'], t3_2['Lat'], c='g', label='Tier3_2')
# plt.scatter(t3_3['Lon'], t3_3['Lat'], c='b', label='Tier3_3')
# plt.scatter(t3_4['Lon'], t3_4['Lat'], c='y', label='Tier3_4')
# plt.scatter(t3_5['Lon'], t3_5['Lat'], c='c', label='Tier3_5')
# plt.scatter(t3_6['Lon'], t3_6['Lat'], c='m', label='Tier3_6')
# plt.scatter(t3_7['Lon'], t3_7['Lat'], c='k', label='Tier3_7')

#Tier 4
# plt.scatter(t4_1['Lon'], t4_1['Lat'], c='r', label='Tier4_1')
# plt.scatter(t4_2['Lon'], t4_2['Lat'], c='g', label='Tier4_2')
# plt.scatter(t4_3['Lon'], t4_3['Lat'], c='b', label='Tier4_3')
# plt.scatter(t4_4['Lon'], t4_4['Lat'], c='y', label='Tier4_4')
# plt.scatter(t4_5['Lon'], t4_5['Lat'], c='c', label='Tier4_5')
# plt.scatter(t4_6['Lon'], t4_6['Lat'], c='m', label='Tier4_6')
# plt.scatter(t4_7['Lon'], t4_7['Lat'], c='k', label='Tier4_7')

#Tier 5
# plt.scatter(t5_1['Lon'], t5_1['Lat'], c='r', label='Tier5_1')
# plt.scatter(t5_2['Lon'], t5_2['Lat'], c='g', label='Tier5_2')
# plt.scatter(t5_3['Lon'], t5_3['Lat'], c='b', label='Tier5_3')
# plt.scatter(t5_4['Lon'], t5_4['Lat'], c='y', label='Tier5_4')
# plt.scatter(t5_5['Lon'], t5_5['Lat'], c='c', label='Tier5_5')
# plt.scatter(t5_6['Lon'], t5_6['Lat'], c='m', label='Tier5_6')
# plt.scatter(t5_7['Lon'], t5_7['Lat'], c='k', label='Tier5_7')

#Tier 6
plt.scatter(t6_1['Lon'], t6_1['Lat'], c='r', label='Tier6_1')
plt.scatter(t6_2['Lon'], t6_2['Lat'], c='g', label='Tier6_2')
plt.scatter(t6_3['Lon'], t6_3['Lat'], c='b', label='Tier6_3')
plt.scatter(t6_4['Lon'], t6_4['Lat'], c='y', label='Tier6_4')
plt.scatter(t6_5['Lon'], t6_5['Lat'], c='c', label='Tier6_5')
plt.scatter(t6_6['Lon'], t6_6['Lat'], c='m', label='Tier6_6')
plt.scatter(t6_7['Lon'], t6_7['Lat'], c='k', label='Tier6_7')



#Each Full Tier

#plt.scatter(prem['Lon'], prem['Lat'], c='r', label='Premier')
#plt.scatter(div1['Lon'], div1['Lat'], c='b', label='North/South1')
#plt.scatter(div2['Lon'], div2['Lat'], c='g', label='North/South2')
#plt.scatter(t1['Lon'], t1['Lat'], c='y', label='Tier1')
#plt.scatter(t2['Lon'], t2['Lat'], c='c', label='Tier2')
#plt.scatter(t3['Lon'], t3['Lat'], c='m', label='Tier3')
#plt.scatter(t4['Lon'], t4['Lat'], c='k', label='Tier4')
#plt.scatter(t5['Lon'], t5['Lat'], c='w', label='Tier5')
#plt.scatter(t6['Lon'], t6['Lat'], c='0.5', label='Tier6')

plt.legend()
plt.show()
