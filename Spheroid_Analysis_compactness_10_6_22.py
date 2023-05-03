import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob
import matplotlib.pyplot as plt

start_time = time.time()
base_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Spheroid analysis'
# base_directory =  os.getcwd() + '\\'

#region Input parameters
# input_dir_base="C:\\Users\\evolo\\OneDrive\\Juanita\\Fucci_analysis\\Parse_CellProfiler_Scripts\\INPUT\\" # do not include the date-subfolder here, that will be pulled automatically
input_dir_base = base_directory + '\\'
save_dir=input_dir_base # you can just write this as << save_dir = input_dir_base  >> if you want to save it in the same base directory as the input files, otherweise specify other directory
file_ending='ResultsMyExpt_EditedObjects_Filtered_by_last_day_merged' #

file_list=glob.glob(save_dir + '\*'+file_ending+'.csv', recursive=True)

df1=pd.read_csv(file_list[0])
df2=pd.read_csv(file_list[1])
df3=pd.read_csv(file_list[2])
df4=pd.read_csv(file_list[3])
df5=pd.read_csv(file_list[4])
df6=pd.read_csv(file_list[5])
df7=pd.read_csv(file_list[6])
df8=pd.read_csv(file_list[7])
df9=pd.read_csv(file_list[8])
df10=pd.read_csv(file_list[9])
df11=pd.read_csv(file_list[10])
df12=pd.read_csv(file_list[11])
df13=pd.read_csv(file_list[12])
df14=pd.read_csv(file_list[13])

df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14])
df = df.reset_index(drop=True)

df['Media_Type']=df['Metadata_Well']

mask_fh1 = df['Metadata_Well'].str.contains(r'B', na=True)
mask_fh2 = df['Metadata_Well'].str.contains(r'C', na=True)
df.loc[mask_fh1, 'Media_Type'] = 'FH'
df.loc[mask_fh2, 'Media_Type'] = 'FH'
mask_hh1 = df['Metadata_Well'].str.contains(r'D', na=True)
mask_hh2 = df['Metadata_Well'].str.contains(r'E', na=True)
df.loc[mask_hh1, 'Media_Type'] = 'HH'
df.loc[mask_hh2, 'Media_Type'] = 'HH'
mask_rh1 = df['Metadata_Well'].str.contains(r'F', na=True)
mask_rh2 = df['Metadata_Well'].str.contains(r'G', na=True)
df.loc[mask_rh1, 'Media_Type'] = 'RH'
df.loc[mask_rh2, 'Media_Type'] = 'RH'

df_means=df.groupby(['Media_Type','Day']).mean()

x_list=['Day 1','Day 2','Day 3','Day 4','Day 5','Day 6','Day 7','Day 8','Day 9','Day 10','Day 11','Day 12','Day 13','Day 14']
sorterIndex = dict(zip(x_list, range(len(x_list))))
# Generate a rank column that will be used to sort
df['Day_Rank'] = df['Day'].map(sorterIndex)
df.sort_values(['Day_Rank'], ascending=[True], inplace=True)
ax = sns.lineplot(x="Day", y='AreaShape_Compactness', data=df, hue="Media_Type",sort=False)

fig = plt.gcf()

fig.set_size_inches(10, 8)

ax.tick_params(direction='in')

plt.savefig(r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Spheroid analysis\lineplot.png')

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))