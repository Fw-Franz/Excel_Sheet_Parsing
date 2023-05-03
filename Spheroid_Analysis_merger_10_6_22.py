import numpy as np
import seaborn as sns
import pandas as pd
import time
import os
import glob

start_time = time.time()
base_directory = r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\Spheroid analysis'
# base_directory =  os.getcwd() + '\\'

#region Input parameters
# input_dir_base="C:\\Users\\evolo\\OneDrive\\Juanita\\Fucci_analysis\\Parse_CellProfiler_Scripts\\INPUT\\" # do not include the date-subfolder here, that will be pulled automatically
input_dir_base = base_directory + '\\'
save_dir=input_dir_base # you can just write this as << save_dir = input_dir_base  >> if you want to save it in the same base directory as the input files, otherweise specify other directory
file_ending='_Filtered_by_last_day' #

file_list=glob.glob(save_dir + '\**\*'+file_ending+'.csv', recursive=True)
df1=pd.read_csv(file_list[0])
df1['ImageObject']=df1['ImageNumber'].astype(str)+'_'+df1['ObjectNumber'].astype(str)
df2=pd.read_csv(file_list[1])
df2['ImageObject']=df2['ImageNumber'].astype(str)+'_'+df2['ObjectNumber'].astype(str)
df3=pd.read_csv(file_list[2])
df3['ImageObject']=df3['ImageNumber'].astype(str)+'_'+df3['ObjectNumber'].astype(str)
df4=pd.read_csv(file_list[3])
df4['ImageObject']=df4['ImageNumber'].astype(str)+'_'+df4['ObjectNumber'].astype(str)
df5=pd.read_csv(file_list[4])
df5['ImageObject']=df5['ImageNumber'].astype(str)+'_'+df5['ObjectNumber'].astype(str)
df6=pd.read_csv(file_list[5])
df6['ImageObject']=df6['ImageNumber'].astype(str)+'_'+df6['ObjectNumber'].astype(str)
df7=pd.read_csv(file_list[6])
df7['ImageObject']=df7['ImageNumber'].astype(str)+'_'+df7['ObjectNumber'].astype(str)
df8=pd.read_csv(file_list[7])
df8['ImageObject']=df8['ImageNumber'].astype(str)+'_'+df8['ObjectNumber'].astype(str)
df9=pd.read_csv(file_list[8])
df9['ImageObject']=df9['ImageNumber'].astype(str)+'_'+df9['ObjectNumber'].astype(str)
df10=pd.read_csv(file_list[9])
df10['ImageObject']=df10['ImageNumber'].astype(str)+'_'+df10['ObjectNumber'].astype(str)
df11=pd.read_csv(file_list[10])
df11['ImageObject']=df11['ImageNumber'].astype(str)+'_'+df11['ObjectNumber'].astype(str)
df12=pd.read_csv(file_list[11])
df12['ImageObject']=df12['ImageNumber'].astype(str)+'_'+df12['ObjectNumber'].astype(str)
df13=pd.read_csv(file_list[12])
df13['ImageObject']=df13['ImageNumber'].astype(str)+'_'+df13['ObjectNumber'].astype(str)
df14=pd.read_csv(file_list[13])
df14['ImageObject']=df14['ImageNumber'].astype(str)+'_'+df14['ObjectNumber'].astype(str)



df=df1.merge(on='ImageObject', right=df2, how='inner', suffixes=['df1', 'df2'])
df=df.merge(on='ImageObject', right=df3, how='inner', suffixes=['', 'df3'])
df=df.merge(on='ImageObject', right=df4, how='inner', suffixes=['', 'df4'])
df=df.merge(on='ImageObject', right=df5, how='inner', suffixes=['', 'df5'])
df=df.merge(on='ImageObject', right=df6, how='inner', suffixes=['', 'df6'])
df=df.merge(on='ImageObject', right=df7, how='inner', suffixes=['', 'df7'])
df=df.merge(on='ImageObject', right=df8, how='inner', suffixes=['', 'df8'])
df=df.merge(on='ImageObject', right=df9, how='inner', suffixes=['', 'df9'])
df=df.merge(on='ImageObject', right=df10, how='inner', suffixes=['', 'df10'])
df=df.merge(on='ImageObject', right=df11, how='inner', suffixes=['', 'df11'])
df=df.merge(on='ImageObject', right=df12, how='inner', suffixes=['', 'df12'])
df=df.merge(on='ImageObject', right=df13, how='inner', suffixes=['', 'df13'])
df=df.merge(on='ImageObject', right=df14, how='inner', suffixes=['', 'df14'])

ImageObject_list=pd.unique(df.ImageObject)

df1 = df1.loc[df1['ImageObject'].isin(ImageObject_list)]
df2 = df2.loc[df2['ImageObject'].isin(ImageObject_list)]
df3 = df3.loc[df3['ImageObject'].isin(ImageObject_list)]
df4 = df4.loc[df4['ImageObject'].isin(ImageObject_list)]
df5 = df5.loc[df5['ImageObject'].isin(ImageObject_list)]
df6 = df6.loc[df6['ImageObject'].isin(ImageObject_list)]
df7 = df7.loc[df7['ImageObject'].isin(ImageObject_list)]
df8 = df8.loc[df8['ImageObject'].isin(ImageObject_list)]
df9 = df9.loc[df9['ImageObject'].isin(ImageObject_list)]
df10 = df10.loc[df10['ImageObject'].isin(ImageObject_list)]
df11 = df11.loc[df11['ImageObject'].isin(ImageObject_list)]
df12 = df12.loc[df12['ImageObject'].isin(ImageObject_list)]
df13 = df13.loc[df13['ImageObject'].isin(ImageObject_list)]
df14 = df14.loc[df14['ImageObject'].isin(ImageObject_list)]

print(len(df1),len(df2),len(df3),len(df4),len(df5),len(df6),len(df7),len(df8),len(df9),len(df10),len(df11),len(df12),len(df13),len(df14))

sorterIndex = dict(zip(ImageObject_list, range(len(ImageObject_list))))
# Generate a rank column that will be used to sort
df1['ImageObject_Rank'] = df1['ImageObject'].map(sorterIndex)
df1.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
# df1.drop('ImageObject_Rank', 1, inplace=True)
df2['ImageObject_Rank'] = df2['ImageObject'].map(sorterIndex)
df2.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df3['ImageObject_Rank'] = df3['ImageObject'].map(sorterIndex)
df3.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df4['ImageObject_Rank'] = df4['ImageObject'].map(sorterIndex)
df4.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df5['ImageObject_Rank'] = df5['ImageObject'].map(sorterIndex)
df5.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df6['ImageObject_Rank'] = df6['ImageObject'].map(sorterIndex)
df6.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df7['ImageObject_Rank'] = df7['ImageObject'].map(sorterIndex)
df7.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df8['ImageObject_Rank'] = df8['ImageObject'].map(sorterIndex)
df8.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df9['ImageObject_Rank'] = df9['ImageObject'].map(sorterIndex)
df9.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df10['ImageObject_Rank'] = df10['ImageObject'].map(sorterIndex)
df10.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df11['ImageObject_Rank'] = df11['ImageObject'].map(sorterIndex)
df11.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df12['ImageObject_Rank'] = df12['ImageObject'].map(sorterIndex)
df12.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df13['ImageObject_Rank'] = df13['ImageObject'].map(sorterIndex)
df13.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)
df14['ImageObject_Rank'] = df14['ImageObject'].map(sorterIndex)
df14.sort_values(['ImageObject_Rank'], ascending=[True], inplace=True)

file=str.replace(file_list[0],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df1['Day']=str.replace(folder_name,' Results','')
df1.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[1],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df2['Day']=str.replace(folder_name,' Results','')
df2.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[2],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df3['Day']=str.replace(folder_name,' Results','')
df3.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[3],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df4['Day']=str.replace(folder_name,' Results','')
df4.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[4],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df5['Day']=str.replace(folder_name,' Results','')
df5.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[5],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df6['Day']=str.replace(folder_name,' Results','')
df6.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[6],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df7['Day']=str.replace(folder_name,' Results','')
df7.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[7],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df8['Day']=str.replace(folder_name,' Results','')
df8.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[8],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df9['Day']=str.replace(folder_name,' Results','')
df9.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[9],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df10['Day']=str.replace(folder_name,' Results','')
df10.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[10],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df11['Day']=str.replace(folder_name,' Results','')
df11.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[11],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df12['Day']=str.replace(folder_name,' Results','')
df12.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[12],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df13['Day']=str.replace(folder_name,' Results','')
df13.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)
file=str.replace(file_list[13],'.csv','_merged.csv',)
folder_name = os.path.basename(os.path.dirname(file))
df14['Day']=str.replace(folder_name,' Results','')
df14.to_csv(path_or_buf=save_dir+folder_name+os.path.basename(file), index=None)

print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))