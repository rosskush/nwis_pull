__author__ = 'rosskush'

# In this simmple example, we will feed the USGS site ID, date ranges, and the param code to retrieve a dataframe 

import os
import sys
# sys.path.append(os.path.join('..','nwis_pull')) # from https://github.com/rosskush/nwis_pull
import nwis_pull as nwis

df = nwis.pull_data.realtime('212214157535401','2017-12-01','2017-12-28','72150')
print(df.head())

# plotting

columns = df.columns

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(df.index,df[columns[-1]])
ax.grid()


# feild data
fdf = nwis.pull_data.field_measurments('212214157535401')

print(fdf.head())
print(fdf.columns)


fig, ax = plt.subplots()
ax.scatter(fdf.index.tolist(),fdf['sl_lev_va'])
ax.grid()

plt.show()

