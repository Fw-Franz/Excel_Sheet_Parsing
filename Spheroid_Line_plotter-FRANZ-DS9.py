import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob
import matplotlib.pyplot as plt
from functools import reduce

start_time = time.time()
base_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Franz_New Data\RH'
# base_directory =  os.getcwd() + '\\'

folder_list=glob.glob(base_directory + '\*/', recursive=True)
# folder_file_list=folder_list+file_list

print(folder_list)

dataframe_collection = {}

# dfs = pd.DataFrame()
for folder in folder_list:
    folder_sub = folder[:-1]
    foldername = os.path.basename(folder_sub)
    df_inter=pd.read_csv(folder+'\\combined_dataframe_Filtered_by_all_days.csv')
    df_inter['Day']=int(foldername[-2:])
    if folder == folder_list[0]:
        dfs=df_inter
    else:
        for obj in df_inter['ObjectNumber'].unique().tolist():
            df_inter.drop(df_inter[~((df_inter['ObjectNumber']==obj) & (df_inter['AreaShape_Area'] > df_inter_last.loc(df_inter_last['ObjectNumber']==obj,'AreaShape_Area').value))].index)
        dfs=pd.concat([dfs,df_inter])

    df_inter_last = df_inter


dfs_well=dfs[dfs['Metadata_Well']=='B2']
# for i in dfs_well['Day'].unique().tolist():
#     if i>4:
#         dfs_well.drop(dfs_well[~((dfs_well['AreaShape_Area'] > 100000))].index)


plt.figure()
ax=sns.lineplot(data=dfs_well, x='Day', y='AreaShape_Area',hue='ObjectNumber')

plt.savefig(base_directory+'\\combined_dataframe_Filtered_by_all_days_lineplot_B2.png')

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))