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

folder_last_day=folder_list[-1]
file_last_day=folder_last_day+'\\MyExpt_FilterObjects2.csv'
df_last_day=pd.read_csv(file_last_day)\

plus_minus_center=100

dfs=[]

for folder in folder_list:
        # dataframe_collection[folder] = pd.read_csv(file)
    df=pd.read_csv(folder+'\\MyExpt_FilterObjects2.csv')

    for well in pd.unique(df_last_day['Metadata_Well']):
        # print('well: ', well)
        df_last_day_welli = df_last_day[df_last_day['Metadata_Well'] == well].copy()
        # print(df_last_day_welli)

        for object in pd.unique(df_last_day_welli['ObjectNumber']):
        # print('object: ', object)

        # query_str = f'Metadata_Well == {well} &ObjectNumber == {object} &  ((Location_Center_X < "{condition}" & group2 == "{control_condition}") | (group1 == "{control_condition}" & group2 == "{condition}"))'
            # df_filtered = df.query(query_str)
            Location_x = df_last_day.loc[(df_last_day['Metadata_Well'] == well) & (
                            df_last_day['ObjectNumber'] == object), 'Location_Center_X'].values[0]
            Location_y = df_last_day.loc[(df_last_day['Metadata_Well'] == well) & (
                        df_last_day['ObjectNumber'] == object), 'Location_Center_Y'].values[0]

            df.loc[(df['Metadata_Well'] == well) & (df['Location_Center_X'] < (Location_x + plus_minus_center)) & (
                        df['Location_Center_X'] > (Location_x - plus_minus_center)) & (df['Location_Center_Y'] < (Location_y + plus_minus_center)) & (
                               df['Location_Center_Y'] > (Location_y - plus_minus_center)), 'object_new'] = object

    # print('df size before filtering: ', df.size)
    size_old = len(df)
    # df=df.loc[pd.notnull(df.object_new)] #also works
    df.dropna(subset=['object_new'], inplace=True)
    # print('df size after filtering: ', df.size)
    size_new = len(df)
    print('old size:', size_old, '--- new size: ', size_new, '--- removed:', size_old - size_new, 'objects')

    df['ObjectNumber'] = df['object_new']
    df.drop('object_new', axis=1, inplace=True)

    df.to_csv(path_or_buf=folder+'\\combined_dataframe_Filtered_by_last_day.csv', index=None)


print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))