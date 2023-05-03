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

factor='f1p5'

dfs=pd.read_csv(base_directory+'\\combined_dataframe_Filtered_by_all_days_for_all_days_duplicates_'+factor+'_removed.csv')


for well_i in dfs['Metadata_Well'].unique().tolist():
    dfs_well=dfs.loc[dfs['Metadata_Well']==well_i]
    plt.figure()
    ax=sns.lineplot(data=dfs_well, x='Day', y='AreaShape_Area',hue='ObjectNumber')

    plt.savefig(base_directory+'\\combined_dataframe_Filtered_by_all_days_lineplot_'+well_i+'_'+factor+'.png')
    plt.close()

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))