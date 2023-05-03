import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob

start_time = time.time()
base_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Clone_Analysis\Colo_ASAP3_clones'
# base_directory =  os.getcwd() + '\\'

#region Input parameters
# input_dir_base="C:\\Users\\evolo\\OneDrive\\Juanita\\Fucci_analysis\\Parse_CellProfiler_Scripts\\INPUT\\" # do not include the date-subfolder here, that will be pulled automatically
input_dir_base = base_directory + '\\'
save_dir=input_dir_base # you can just write this as << save_dir = input_dir_base  >> if you want to save it in the same base directory as the input files, otherweise specify other directory
file_ending='object' #

file_list=glob.glob(save_dir + '\**\*'+file_ending+'.csv', recursive=True)
for file in file_list:

    print('processing: ',file)

    df=pd.read_csv(file,skiprows=17)

    df=df[df['Class 1']==True]
    df.loc[:, 'Target 2-to-3 Mean Intensity ratio'] = (df.loc[:, 'Target 2: Mean Intensity']) / (df.loc[:,'Target 3: Mean Intensity'])

    file_ratios=str.replace(file,'.csv','_Class_1_True_wt_mean_int_2_3_ratios.csv',)
    df.to_csv(path_or_buf=file_ratios, index=None)

    df_well_means = df.groupby(['Well'], sort=False).mean()
    df_well_stds = df.groupby(['Well'], sort=False).std()

    file_means=str.replace(file,'.csv','_Class_1_True_well_means.csv',)
    df_well_means.to_csv(path_or_buf=file_means, index=None)
    file_stds=str.replace(file,'.csv','_Class_1_True_well_stds.csv',)
    df_well_stds.to_csv(path_or_buf=file_stds, index=None)

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))