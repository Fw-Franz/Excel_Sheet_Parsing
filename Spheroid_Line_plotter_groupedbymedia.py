import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob
import matplotlib.pyplot as plt
from functools import reduce

start_time = time.time()
## directory Franz
base_directory = r'C:\Users\evolo\OneDrive\Juanita\Spheroids\Spheroid_mixed\Raw_Analysis_Mixed_ori'

directory_list=[base_directory]
## directory Juanita
# base_directory = r'C:\Users\evolover\OneDrive\Juanita\Spheroids\Franz_New Data\HF'

factor='f10'

normalization_to_day_0=True

for directory in directory_list:

    print('working on ', directory)

    # dfs = pd.read_csv(
    #     base_directory + '\\combined_dataframe_Filtered_by_all_days_for_all_days_duplicates_' + factor + '_removed.csv')
    dfs = pd.read_csv(
        directory + '\\combined_dataframe_Filtered_by_all_days_for_all_days_duplicates_' + factor + '_removed.csv')

    dfs = dfs[dfs['Day'] > -1]

    plot_item_list_1 = ['Intensity_MeanIntensity_CropBlue', 'Intensity_IntegratedIntensity_CropBlue',
                        'Intensity_MedianIntensity_CropBlue', 'Intensity_StdIntensity_CropBlue',
                        'Intensity_MADIntensity_CorrBlue', 'AreaShape_Area', 'AreaShape_FormFactor',
                        'AreaShape_Compactness', 'AreaShape_Eccentricity', 'AreaShape_Solidity']

    plot_item_list_2=['AreaShape_Area', 'AreaShape_FormFactor', 'AreaShape_Compactness', 'AreaShape_Eccentricity', 'AreaShape_Solidity']

    # divide_by_plot_item_list=[True, False]firstTrue
    divide_by_plot_item_list=[False]

    for divide_by_plot_item_2 in divide_by_plot_item_list:
        if divide_by_plot_item_2 == True:
            plot_item_list2=plot_item_list_2
        else:
            plot_item_list2=[plot_item_list_2[0]]

        for plot_item_1 in plot_item_list_1:

            print('plotting for', plot_item_1)

            for plot_item_2 in plot_item_list2:

                if divide_by_plot_item_2 == True:
                    if plot_item_1 == plot_item_2:
                        continue

                save_string_1=plot_item_1.replace('Intensity_','')
                save_string_2=plot_item_2.replace('Intensity_','')

                save_string_1=save_string_1.replace('CropBlue','')
                save_string_2=save_string_2.replace('CropBlue','')

                # start_day=dfs['Day'].min()
                # dfs_groups=dfs.groupby([ 'Day', 'ImageNumber','ObjectNumber'])}
                # for (Day, ImageNumber, ObjectNumber), group in groups.items():
                #     start_day_group = groups[(dfs.start_day(), ObjectNumber, Day, ImageNumber)]
                #     group['Normalized_to_Day8'] = group['AreaShape_Area'] / start_day_group['AreaShape_Area']

                # dfs['Normalized_to_Day8'] = dfs['AreaShape_Area'].div(dfs.groupby(['Day','ObjectNumber', 'ImageNumber'], sort=True)['AreaShape_Area'].transform('first'))

                days_list=dfs['Day'].unique().tolist()
                # object_list=dfs['object_id'].unique().tolist()
                for Day in days_list:
                    object_list = dfs.loc[(dfs['Day']==Day),'object_id'].unique().tolist()
                    for object_id in object_list:
                        if normalization_to_day_0:
                            if divide_by_plot_item_2:
                                dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),'Normalized_to_Day0'] = \
                                    (dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_1].values[0] /
                                     dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==days_list[0]),plot_item_1].values[0])\
                                       /(dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_2].values[0] /
                                     dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==days_list[0]),plot_item_2].values[0])
                            else:
                                dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),'Normalized_to_Day0'] = \
                                    (dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_1].values[0] /
                                     dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==days_list[0]),plot_item_1].values[0])
                        else:
                            if divide_by_plot_item_2:
                                dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),'Normalized_to_Day0'] = \
                                    dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_1].values[0] \
                                     /dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_2].values[0]
                            else:
                                dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),'Normalized_to_Day0'] = \
                                    dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_1].values[0]





                media_list = ['HH', 'HF', 'RF', 'RH']

                for well_i in dfs['Metadata_Well'].unique().tolist():

                    if "B" in well_i or "C" in well_i :
                        dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[0]
                        # print(well_i, media_list[0])
                    if "D" in well_i or "E" in well_i :
                        dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[1]
                        # print(well_i, media_list[1])
                    if ("F" in well_i or "G" in well_i) and ("2" in well_i or "3" in well_i or "4" in well_i or "5" in well_i or "6" in well_i) :
                        dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[2]
                        # print(well_i, media_list[2])
                    if ("F" in well_i or "G" in well_i) and ("7" in well_i or "8" in well_i or "9" in well_i or "10" in well_i or "11" in well_i) :
                        dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[3]
                        # print(well_i, media_list[3])

                plt.figure()

                if normalization_to_day_0:
                    norm_string=' normalized to day 0'
                else:
                    norm_string = ''

                if divide_by_plot_item_2:
                    y_title='(' +save_string_1+' / '+save_string_2 + ')' + norm_string
                else:
                    y_title=save_string_1+ norm_string

                ax=sns.lineplot(data=dfs, x='Day', y='Normalized_to_Day0', hue='Media')

                #  Returns tuple of handles, labels for axis ax, after reordering them to conform to the label order `order`, and if unique is True, after removing entries with duplicate labels.
                def reorderLegend(ax=None,order=None,unique=False):
                    if ax is None: ax=plt.gca()
                    handles, labels = ax.get_legend_handles_labels()
                    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0])) # sort both labels and handles by labels
                    if order is not None: # Sort according to a given list (not necessarily complete)
                        keys=dict(zip(order,range(len(order))))
                        labels, handles = zip(*sorted(zip(labels, handles), key=lambda t,keys=keys: keys.get(t[0],np.inf)))
                    if unique:  labels, handles= zip(*unique_everseen(zip(labels,handles), key = labels)) # Keep only the first of each handle
                    ax.legend(handles, labels)
                    return(handles, labels)


                def unique_everseen(seq, key=None):
                    seen = set()
                    seen_add = seen.add
                    return [x for x,k in zip(seq,key) if not (k in seen or seen_add(k))]

                reorderLegend(ax,media_list)

                # handles, labels = ax.get_legend_handles_labels()
                # # sort both labels and handles by labels
                # labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
                # ax.legend(handles, labels)

                plt.ylabel(y_title)
                if normalization_to_day_0:
                    save_norm_string='_Day0_normalized'
                else:
                    save_norm_string=''
                if divide_by_plot_item_2:
                    plt.savefig(directory+'\\lineplot'+save_norm_string+'_grouped_'+save_string_1+'_by_'+save_string_2+'.png')
                else:
                    plt.savefig(directory+'\\lineplot'+save_norm_string+'_grouped_'+save_string_1+'.png')
                plt.close()

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))