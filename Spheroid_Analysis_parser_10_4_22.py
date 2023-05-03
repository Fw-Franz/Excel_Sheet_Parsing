import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob

start_time = time.time()
base_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Spheroid analysis'
last_day_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Spheroid analysis\Day 14 Results'
# base_directory =  os.getcwd() + '\\'

#region Input parameters
# input_dir_base="C:\\Users\\evolo\\OneDrive\\Juanita\\Fucci_analysis\\Parse_CellProfiler_Scripts\\INPUT\\" # do not include the date-subfolder here, that will be pulled automatically
input_dir_base = base_directory + '\\'
save_dir=input_dir_base # you can just write this as << save_dir = input_dir_base  >> if you want to save it in the same base directory as the input files, otherweise specify other directory
file_ending='MyExpt_EditedObjects' #

file_list_last_day=glob.glob(last_day_directory+'\\' + '\*'+file_ending+'.csv', recursive=True)

for file in file_list_last_day:

    print('processing last day file: ',file)

    df_last_day = pd.read_csv(file)



    # for each imageNum, get x and y locations, then search for each ImageNum in other  days and delate other objects, and rename these objects to same number as in day 14

file_list=glob.glob(save_dir + '\**\*'+file_ending+'.csv', recursive=True)
for file in file_list:

    print('processing: ',file)

    df=pd.read_csv(file)

    # df_last_day['Image_and_Object_Number']=df_last_day['ImageNumber']+df_last_day['ObjectNumber']

    for image in pd.unique(df_last_day['ImageNumber']):
        # print('image: ', image)
        df_last_day_imagei=df_last_day[df_last_day['ImageNumber']==image].copy()
        # print(df_last_day_imagei)

        for object in pd.unique(df_last_day_imagei['ObjectNumber']):
            # print('object: ', object)

            # query_str = f'ImageNumber == {image} &ObjectNumber == {object} &  ((Location_Center_X < "{condition}" & group2 == "{control_condition}") | (group1 == "{control_condition}" & group2 == "{condition}"))'
            # df_filtered = df.query(query_str)
            Location_x=df_last_day.loc[(df_last_day['ImageNumber']==image)&(df_last_day['ObjectNumber']==object),'Location_Center_X'].values[0]
            Location_y=df_last_day.loc[(df_last_day['ImageNumber']==image)&(df_last_day['ObjectNumber']==object),'Location_Center_Y'].values[0]

            df.loc[(df['ImageNumber']==image)&(df['Location_Center_X']<(Location_x+50))&(df['Location_Center_X']>(Location_x-50))&(df['Location_Center_Y']<(Location_y+50))&(df['Location_Center_Y']>(Location_y-50)), 'object_new']=object

    # print('df size before filtering: ', df.size)
    size_old=len(df)
    # df=df.loc[pd.notnull(df.object_new)] #also works
    df.dropna(subset=['object_new'], inplace=True)
    # print('df size after filtering: ', df.size)
    size_new=len(df)
    print('old size:',size_old, 'new size: ',size_new, 'removed:', size_old-size_new, 'objects')

    df['ObjectNumber']=df['object_new']
    df.drop('object_new', axis=1, inplace=True)

    file_filtered=str.replace(file,'.csv','_Filtered_by_last_day.csv',)
    df.to_csv(path_or_buf=file_filtered, index=None)


print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))