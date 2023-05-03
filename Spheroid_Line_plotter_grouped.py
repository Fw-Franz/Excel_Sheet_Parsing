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
base_directory = r'C:\Users\evolo\OneDrive\Juanita\Spheroids\Franz_New Data'
folder_list=glob.glob(base_directory + '\*/', recursive=False)

# directory_list=[base_directory]
directory_list=folder_list
## directory Juanita
# base_directory = r'C:\Users\evolover\OneDrive\Juanita\Spheroids\Franz_New Data\HF'

factor='f1p5'

# drug='5-FU'  # '5-FU', 'CPT-11', or 'Oxaliplatin'
#drug_list=['5-FU', 'CPT-11', 'Oxaliplatin',]
drug_list=['CPT-11']

for drug in drug_list:

    for directory in directory_list:

        print('working on ', directory, drug)

        # dfs = pd.read_csv(
        #     base_directory + '\\combined_dataframe_Filtered_by_all_days_for_all_days_duplicates_' + factor + '_removed.csv')
        dfs = pd.read_csv(
            directory + '\\combined_dataframe_Filtered_by_all_days_for_all_days_duplicates_' + factor + '_removed.csv')

        dfs = dfs[dfs['Day'] >6]

        #plot_item_list_1=['Intensity_MeanIntensity_CropBlue', 'Intensity_IntegratedIntensity_CropBlue', 'Intensity_MedianIntensity_CropBlue', 'Intensity_StdIntensity_CropBlue', 'Intensity_MADIntensity_CorrBlue', 'AreaShape_Area', 'AreaShape_FormFactor', 'AreaShape_Compactness', 'AreaShape_Eccentricity', 'AreaShape_Solidity']
        plot_item_list_1 = ['AreaShape_FormFactor', 'AreaShape_Area']
        plot_item_list_2 = ['AreaShape_FormFactor', 'AreaShape_Area']
       # plot_item_list_2 = ['AreaShape_Area', 'AreaShape_FormFactor',]
       # plot_item_list_2=['AreaShape_Area', 'AreaShape_FormFactor', 'AreaShape_Area', 'AreaShape_Compactness', 'AreaShape_Eccentricity', 'AreaShape_Solidity']

        # divide_by_plot_item_list=[True, False]firstTrue
        divide_by_plot_item_list=[False]

        for divide_by_plot_item_2 in divide_by_plot_item_list:
            if divide_by_plot_item_2 == True:
                plot_item_list2=plot_item_list_2
            else:
                plot_item_list2=[plot_item_list_2[0]]

            for plot_item_1 in plot_item_list_1:

                for plot_item_2 in plot_item_list2:

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
                            if divide_by_plot_item_2:
                                dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),'Normalized_to_Day7'] = \
                                    (dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_1].values[0] /
                                     dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==days_list[0]),plot_item_1].values[0])\
                                       /(dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_2].values[0] /
                                     dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==days_list[0]),plot_item_2].values[0])
                            else:
                                dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),'Normalized_to_Day7'] = \
                                    (dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==Day),plot_item_1].values[0] /
                                     dfs.loc[(dfs['object_id']==object_id) & (dfs['Day']==days_list[0]),plot_item_1].values[0])\

                    group=['X2','X3','Y2','Y3','X4','X5','Y4','Y5','X6','X7','Y6','Y7','X8','X9','Y8','Y9','X10','X11','Y10','Y11']

                    # group1=['B2','B3','C2','C3']
                    # group2=['B4','B5','C4','C5']
                    # group3=['B6','B7','C6','C7']
                    # group4=['B8','B9','C8','C9']
                    # group5=['B10','B11','C10','C11']

                    #if drug=='5-FU':
                       # group = [w.replace('X', 'B') for w in group]
                       # group = [w.replace('Y', 'C') for w in group]
                       # media_list = [u'0 \u03bcM', u'12.5 \u03bcM', u'25 \u03bcM', u'50 \u03bcM', u'100 \u03bcM']
                    if drug == 'CPT-11':
                        group = [w.replace('X', 'D') for w in group]
                        group = [w.replace('Y', 'E') for w in group]
                        media_list = [u'0 \u03bcM', u'2.5 \u03bcM', u'5 \u03bcM', u'10 \u03bcM', u'20 \u03bcM']
                    #elif drug=='CPT-11':
                        #group = [w.replace('X', 'D') for w in group]
                        #group = [w.replace('Y', 'E') for w in group]
                        #media_list = [u'0 \u03bcM', u'2.5 \u03bcM', u'5 \u03bcM', u'10 \u03bcM', u'20 \u03bcM']

                    #elif drug=='Oxaliplatin':
                        #group = [w.replace('X', 'F') for w in group]
                       # group = [w.replace('Y', 'G') for w in group]
                       # media_list = [u'0 \u03bcM', u'5 \u03bcM', u'10 \u03bcM', u'20 \u03bcM', u'40 \u03bcM']

                    # media_list=['0 uM','12.5 uM','25 uM','50 uM','100 uM']
                   # media_list=[u'0 \u03bcM',u'12.5 \u03bcM',u'25 \u03bcM',u'50 \u03bcM',u'100 \u03bcM']
         #Amiloride media_list = ['1000 nM', '500 nM', '250 nM', '125 nM', '0 nM']
         #I3C       media_list = [u'600 \u03bcM', u'300 \u03bcM', u'150 \u03bcM', u'75 \u03bcM', u'0 \u03bcM']
         #5-FU      media_list = [u'0 \u03bcM', u'12.5 \u03bcM', u'25 \u03bcM', u'50 \u03bcM', u'100 \u03bcM']
        #CPT-11     media_list = [u'0 \u03bcM', u'2.5 \u03bcM', u'5 \u03bcM', u'10 \u03bcM', u'20 \u03bcM']
        #Oxal       media_list = [u'0 \u03bcM', u'5 \u03bcM', u'10 \u03bcM', u'20 \u03bcM', u'40 \u03bcM']
        # Mon       media_list = [u'4 \u03bcM', u'2 \u03bcM', u'1 \u03bcM', u'0.5 \u03bcM', u'0 \u03bcM']
         #Val       media_list = [u'2 \u03bcM', u'1 \u03bcM', u'0.5 \u03bcM', u'0.25 \u03bcM', u'0 \u03bcM']
        #VBIT-12    media_list = [u'20 \u03bcM', u'10 \u03bcM', u'5 \u03bcM', u'2.5 \u03bcM', u'0 \u03bcM']
           #MonL    media_list = ['20 nM', '10 nM', '5 nM', '2.5 nM', '0 nM']
          # ValL    media_list = ['100 nM', '50 nM', '25 nM', '12.5 nM', '0 nM']
           # Pin    media_list = ['400 nM', '200 nM', '100 nM', '50 nM', '0 nM']
          # Clof    media_list = [u'5 \u03bcM', u'2.5 \u03bcM', u'1.25 \u03bcM', u'.6125 \u03bcM', u'0 \u03bcM']
          # Sota    media_list = ['1000 nM', '500 nM', '250 nM', '125 nM', '0 nM']
          # TTX     media_list = ['2000 nM', '1000 nM', '500 nM', '250 nM', '0 nM']
                    for well_i in dfs['Metadata_Well'].unique().tolist():
                        # if well_i in group1:
                        #     dfs.loc[dfs['Metadata_Well']==well_i,'Media']=media_list[0]
                        # if well_i in group2:
                        #     dfs.loc[dfs['Metadata_Well']==well_i,'Media']=media_list[1]
                        # if well_i in group3:
                        #     dfs.loc[dfs['Metadata_Well']==well_i,'Media']=media_list[2]
                        # if well_i in group4:
                        #     dfs.loc[dfs['Metadata_Well']==well_i,'Media']=media_list[3]
                        # if well_i in group5:
                        #     dfs.loc[dfs['Metadata_Well']==well_i,'Media']=media_list[4]

                        if well_i in group[0:3]:
                            dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[0]
                        if well_i in group[4:7]:
                            dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[1]
                        if well_i in group[8:11]:
                            dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[2]
                        if well_i in group[12:15]:
                            dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[3]
                        if well_i in group[16:19]:
                            dfs.loc[dfs['Metadata_Well'] == well_i, 'Media'] = media_list[4]

                    plt.figure()

                    if divide_by_plot_item_2:
                        y_title='(' +save_string_1+' / '+save_string_2 + ')' +' normalized to day 7'
                    else:
                        y_title=save_string_1+ ' normalized to day 7'

                    ax=sns.lineplot(data=dfs, x='Day', y='Normalized_to_Day7', hue='Media')

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
                    if divide_by_plot_item_2:
                        plt.savefig(directory+'\\lineplot_Day7_normalized_grouped_'+drug+'_'+save_string_1+'_by_'+save_string_2+'.png')
                    else:
                        plt.savefig(directory+'\\lineplot_Day7_normalized_grouped_'+drug+'_'+save_string_1+'.png')
                    plt.close()

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))