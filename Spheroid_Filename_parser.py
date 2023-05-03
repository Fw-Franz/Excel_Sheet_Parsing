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
# base_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\CellReporter_Data_Franz\I3C'
## directory Juanita
base_directory = r'C:\Users\evolo\OneDrive\Juanita\Spheroids\CellReporter_Data_Franz\I3C'

###################
x_variable='Concentration'
y_variable1='Median_IdentifySecondaryObjects_AreaShape_MeanRadius'
y_variable2='StDev_IdentifySecondaryObjects_AreaShape_MeanRadius'
ylabel1='Area Shape Mean Radius'
hue_variable=''   # if you  don't wannt all drugs in one graph with differnt colors, just type '', otherwise: 'Drug'

custom_stds=False

boxplots=True
scatterplots=True
plot_std_boxplots=False

colors=sns.color_palette("mako", 5)
####################


df=pd.read_csv(base_directory+'/MyExpt_Image.csv')

df['substrings'] = df['FileName_CellImage1'].str.split("_")

df['Length'] = df.substrings.apply(lambda x: len(x))

def decimal_writer(d):
    d[1]=d[1]+'.'+d[2]
    d.pop(2)
    return d

df['substrings'] = df.apply(lambda x: decimal_writer(x['substrings']) if x['Length'] == 9 else x['substrings'], axis=1)

df['Length'] = df.substrings.apply(lambda x: len(x))

df['Trial']=df['substrings'][:].str[0]
df['Concentration']=df['substrings'][:].str[1]
df['Drug']=df['substrings'][:].str[2]

df.drop(columns=['substrings'],inplace=True)

df.to_csv(base_directory+'/MyExpt_Image_split.csv',index=False)


custom_order=(df['Concentration'].unique().tolist())
int_list=list(map(int, custom_order))
int_list.sort()
int_list=list(map(str, int_list))

# df.sort(['Concentration'], ascending = [int_list])
# df['Concentration']=df['Concentration'].astype('int')


plt.figure()

if boxplots:
    if not len(hue_variable)==0:
        ax=sns.boxplot(data=df, x=x_variable, y=y_variable1, hue=hue_variable, orient='v',order=int_list)
    else:
        ax=sns.boxplot(data=df, x=x_variable, y=y_variable1, orient='v',order=int_list,palette=colors, hue_order=int_list)


if custom_stds:
    df['squared_stds']=df[y_variable2].apply(np.square)
    df_sum_sq_stds=df.groupby(["Concentration"])['squared_stds'].apply(sum)/len(df.Trial.unique())
    df_sqrt_sum_sq_stds=df_sum_sq_stds.apply(np.sqrt)
    # df['sqrt_std']=df[y_variable2].apply(np.square).apply(np.sum)/len(df.Trial.unique()).apply(np.sqrt)
    # df['sqrt_std']=(df[y_variable2].apply(np.square)).apply(np.sqrt)

if scatterplots:

    ax = sns.pointplot(data=df, x=x_variable, y=y_variable1, order=int_list, dodge=True,
                           join=False,
                           errorbar=None,color='black')
    if not boxplots:
        if custom_stds:
            x_coords = []
            y_coords = []
            for point_pair in ax.collections:
                for x, y in point_pair.get_offsets():
                    x_coords.append(x)
                    y_coords.append(y)
            # Calculate the type of error to plot as the error bars
            # Make sure the order is the same as the points were looped over
            errors = df_sqrt_sum_sq_stds
            ax.errorbar(x_coords, y_coords, yerr=errors, fmt=' ', zorder=-1, ecolor=colors)

            ymax=max(df[y_variable1])+max(df_sqrt_sum_sq_stds)
            ymin=min(df[y_variable1])-min(df_sqrt_sum_sq_stds)
            ax.set_ylim(ymin, ymax)


        if not len(hue_variable)==0:
            ax=sns.stripplot(data=df, x=x_variable, y=y_variable1, hue=hue_variable, order=int_list)
        else:
            ax=sns.stripplot(data=df, x=x_variable, y=y_variable1,order=int_list, hue="Concentration", palette=colors, hue_order=int_list, legend=False)
    else:
        ax=sns.stripplot(data=df, x=x_variable, y=y_variable1,order=int_list, legend=False,color='grey',edgecolor='white',linewidth=1)

plt.ylabel(ylabel1)
    # y_mean = df.groupby('Concentration').mean()[y_variable1]
    # x = y_mean.index
    # ax.errorbar(x, y_mean, df_sqrt_sum_sq_stds, order=int_list)
if not custom_stds:
    if boxplots:
        plt.savefig(base_directory+'/boxplot_'+y_variable1+'.png')
    elif scatterplots:
        plt.savefig(base_directory+'/scatterplot_'+y_variable1+'.png')

else:
    plt.savefig(base_directory+'/square_stds_'+y_variable1+'.png')

plt.close()

if plot_std_boxplots:
    plt.figure()
    if not len(hue_variable)==0:
        sns.boxplot(data=df, x=x_variable, y=y_variable2, hue=hue_variable, orient='v')
    else:
        sns.boxplot(data=df, x=x_variable, y=y_variable2, orient='v')

    plt.savefig(base_directory+'/boxplot_'+y_variable2+'.png')
    plt.close()



# df['substrings2']=df['substrings']
# df['substrings2'] = df.loc[['Length']==9,]
# df['pos']=
# if
# df['end_position_Trial_Number'] = df['FileName_CellImage1'].str.find('_')
#
# # df['Trial_Number'] = df.FileName_CellImage1.str[:1]
# df['Trial_Number'] = df.apply(lambda x: x['FileName_CellImage1'][0:x['end_position_Trial_Number']],axis=1)

# df['Concentration'] = df.FileName_CellImage1.str[:1]

