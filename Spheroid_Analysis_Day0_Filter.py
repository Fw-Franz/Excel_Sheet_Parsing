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

folder_first_day=folder_list[0]
file_first_day=folder_first_day+'\\combined_dataframe_Filtered_by_last_day.csv'
df_first_day=pd.read_csv(file_first_day)

median_threshold=1.5

# print('df size before filtering: ', df.size)
size_old = len(df_first_day)
# df=df.loc[pd.notnull(df.object_new)] #also works
median_area=df_first_day.AreaShape_Area.median()
df=df_first_day[df_first_day.AreaShape_Area<median_threshold*median_area]
# print('df size after filtering: ', df.size)
size_new = len(df)
print('old size:', size_old, '--- new size: ', size_new, '--- removed:', size_old - size_new, 'objects')

df_first_day.to_csv(path_or_buf=file_first_day.replace('.csv','_unfiltered.csv'), index=None)
df.to_csv(path_or_buf=file_first_day, index=None)


print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))