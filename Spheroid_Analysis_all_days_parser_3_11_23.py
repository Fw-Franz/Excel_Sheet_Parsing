import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob
from functools import reduce

start_time = time.time()
base_directory = r'C:\Users\evolo\OneDrive\Juanita\Spheroids\Spheroid_mixed\Raw_Analysis_Mixed_ori'
# base_directory =  os.getcwd() + '\\'

folder_list=glob.glob(base_directory + '\*\\', recursive=True)
file_list=glob.glob(folder_list[0] + '\**Objects*', recursive=True)
filename_list=[os.path.basename(file_list[0]),os.path.basename(file_list[1]),os.path.basename(file_list[2])]
# folder_file_list=folder_list+file_list

print(folder_list)

dataframe_collection = {}

dfs = []
for folder in folder_list:
    df_inter=pd.read_csv(folder+'\\combined_dataframe_Filtered_by_last_day.csv')
    df_inter['object_id']=df_inter['ImageNumber'].astype(str) +'_'+ df_inter['ObjectNumber'].astype(str)
    dfs.append(df_inter)
    # cols_to_use = df2.columns.difference(df.columns)
# final_df = reduce(lambda left, right: pd.merge(left, right, on=['ObjectNumber'], indicator='Exist'), dfs)#.fillna('none')

for i, dfi in enumerate(dfs):
    for j, dfj in enumerate(dfs):
        # print('before: ',len(dfi),len(dfj))
        dfs[i] = dfi[dfi['object_id'].isin(dfj['object_id'])]
        dfs[j] = dfj[dfj['object_id'].isin(dfi['object_id'])]
        # print('after: ',len(dfi),len(dfj))

for i, folder in enumerate(folder_list):
    print(len(dfs[i]))
    dfs[i].to_csv(path_or_buf=folder + '\\combined_dataframe_Filtered_by_all_days.csv', index=None)



print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))