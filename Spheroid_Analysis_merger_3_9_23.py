import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob
from functools import reduce

start_time = time.time()
base_directory = r'C:\Users\evolo\OneDrive\Juanita\Spheroids\Franz_New Data'
# base_directory =  os.getcwd() + '\\'

folder_list=glob.glob(base_directory + '\*\\', recursive=True)
file_list1=glob.glob(folder_list[0] + '\**MyExpt_FilterObjects1*', recursive=True)
file_list2=glob.glob(folder_list[0] + '\**MyExpt_IdentifyPrimaryObjects*', recursive=True)
print(folder_list)
filename_list=[os.path.basename(file_list1[0]),os.path.basename(file_list2[0])]

# folder_file_list=folder_list+file_list


print(folder_list)

dataframe_collection = {}

for folder in folder_list:
    dfs = []
    for file in filename_list:
        # dataframe_collection[folder] = pd.read_csv(file)
        dfs.append(pd.read_csv(folder+'\\'+file))
    # cols_to_use = df2.columns.difference(df.columns)
    final_df = reduce(lambda left, right: pd.merge(left, right, on=['Location_Center_X','Location_Center_Y'],
                                                   how='inner', suffixes=('', '_duplicate')), dfs)#.fillna('none')

    final_df.to_csv(folder+'\combined_dataframe.csv')

    print('done with ', os.path.basename(folder), ' with shape: ', final_df.shape)


print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))