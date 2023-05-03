import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob
import matplotlib.pyplot as plt
from functools import reduce


factor=10

start_time = time.time()
base_directory = r'C:\Users\evolo\OneDrive\Juanita\Spheroids\Spheroid_mixed\Raw_Analysis_Mixed_ori'
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
        df_inter_last = df_inter.copy()
    else:
        if int(foldername[-2:])>-1:

            size_old = df_inter.size
            print("mean last frame:", df_inter_last[ 'AreaShape_Area'].mean())
            print("mean current frame:", df_inter[ 'AreaShape_Area'].mean())

            for well in df_inter['Metadata_Well'].unique().tolist():
                for obj in df_inter.loc[(df_inter['Metadata_Well']==well),'ObjectNumber'].unique().tolist():
                    # print(folder, well, obj)
                    # df_inter.drop(df_inter[~((df_inter['ObjectNumber']==obj) & (df_inter['Metadata_Well']==well) & (df_inter['AreaShape_Area'] > 2 * df_inter_last.loc[(df_inter_last['ObjectNumber']==obj)&(df_inter_last['Metadata_Well']==well),'AreaShape_Area'].values[0]))].index,inplace=True)
                    if not df_inter_last.loc[(df_inter_last['ObjectNumber']==obj)&(df_inter_last['Metadata_Well']==well),'AreaShape_Area'].empty:
                        # print("last frame:", df_inter_last.loc[(df_inter_last['ObjectNumber'] == obj) & (df_inter_last['Metadata_Well'] == well), 'AreaShape_Area'].values[0])
                        # print("current frame:", df_inter.loc[(df_inter['ObjectNumber'] == obj) & (df_inter['Metadata_Well'] == well), 'AreaShape_Area'].values[0])
                        df_inter.drop(df_inter[(df_inter['ObjectNumber']==obj) & (df_inter['Metadata_Well']==well) & (df_inter['AreaShape_Area'] > factor * df_inter_last.loc[(df_inter_last['ObjectNumber']==obj)&(df_inter_last['Metadata_Well']==well),'AreaShape_Area'].values[0])].index,inplace=True)
                    else:
                        df_inter.drop(df_inter[(df_inter['ObjectNumber'] == obj) & (df_inter['Metadata_Well'] == well)].index,inplace=True)
            print(folder, "before:", size_old, "after:",df_inter.size)
            dfs=pd.concat([dfs,df_inter])

            df_inter_last = df_inter.copy()

dfs.to_csv(base_directory+'\\combined_dataframe_Filtered_by_all_days_for_all_days_duplicates_f'+str(factor).replace('.','p')+'_removed.csv')

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))