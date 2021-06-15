import numpy as np
import seaborn as sns
import pandas as pd
import time
import os

start_time = time.time()
base_directory =  os.getcwd() + '\\'

#region Input parameters
# input_dir_base="C:\\Users\\evolo\\OneDrive\\Juanita\\Fucci_analysis\\Parse_CellProfiler_Scripts\\INPUT\\" # do not include the date-subfolder here, that will be pulled automatically
input_dir_base = base_directory + "Juanita's parsing\\4_8_21\\notdone\\LC3_4_8_21\\"
save_dir=input_dir_base # you can just write this as << save_dir = input_dir_base  >> if you want to save it in the same base directory as the input files, otherweise specify other directory
date='05_13_2021' # sth like '01_21_2021'


#endregion

input_fname_GFAP="GFAP.csv"
input_fname_nuclei="Nuclei.csv"
input_fname_positive_cells="PositiveCells.csv"

print('loading data ... ')
df_GFAP=pd.read_csv(input_dir_base+input_fname_GFAP)
df_nuclei=pd.read_csv(input_dir_base+input_fname_nuclei)
df_positive_cells=pd.read_csv(input_dir_base+input_fname_positive_cells)

image_n=df_GFAP.ImageNumber.tolist()# total number of wells
image_n = list(dict.fromkeys(image_n))
# print(type(image_n))

mi = pd.DataFrame(data=None, index=None, columns=['Row', 'Column', 'Frame', 'DAPI_int_I', 'DAPI_area', 'FarRed_int_I', 'FarRed_area', 'Cell_Num','Cell_Num_Positive', 'Cell_Percent_Positive'])


# for image in image_n[0:100]:  # for testing out a subset
for image in image_n:
    # print('-------------------')
    print('processing image ',image)
    # print('-------------------')

    dfi_GFAP = df_GFAP[(df_GFAP.ImageNumber == image)]

    dfi_nuclei = df_nuclei[(df_nuclei.ImageNumber == image)]
    dfi_n_i=len(dfi_nuclei.index)

    dfi_positive_cells = df_positive_cells[(df_positive_cells.ImageNumber == image)]
    dfi_positive_cells_n_i=len(dfi_positive_cells.index)

    for ObjectNumber in dfi_GFAP.ObjectNumber.tolist():
        dfii_GFAP=dfi_GFAP[(dfi_GFAP.ObjectNumber == ObjectNumber)]
        dfii_nuclei=dfi_nuclei[(dfi_nuclei.ObjectNumber == ObjectNumber)]

        name=dfii_GFAP['FileName_DisplayImage'].values[0]
        row=name[21]
        col=name[22:24]
        frame=name[24:27]

        # print(dfii['Intensity_IntegratedIntensity_OrigBlue'].values[0])
        new_row= {'Row':row, 'Column':col, 'Frame':frame,
                  'DAPI_int_I':dfii_GFAP['Intensity_IntegratedIntensity_OrigBlue'].values[0],
                  'DAPI_area':dfii_nuclei['AreaShape_Area'].values[0],
                  'FarRed_int_I':dfii_GFAP['Intensity_IntegratedIntensity_OrigGreen'].values[0],
                  'FarRed_area':dfii_GFAP['AreaShape_Area'].values[0], 'Cell_Num':dfi_n_i,
                  'Cell_Num_Positive':dfi_positive_cells_n_i, 'Cell_Percent_Positive':dfi_positive_cells_n_i/dfi_n_i}
        mi=mi.append(new_row, ignore_index=True)

mi['DAPI_area'] = mi['DAPI_area'].astype(float)
mi['FarRed_area'] = mi['FarRed_area'].astype(float)
mi['Cell_Num'] = mi['Cell_Num'].astype(float)
mi['Cell_Num_Positive'] = mi['Cell_Num_Positive'].astype(float)
mi['Cell_Percent_Positive'] = mi['Cell_Percent_Positive'].astype(float)

means_frame=mi.groupby(['Row', 'Column', 'Frame'], as_index=False).mean()
stds_frame=mi.groupby(['Row', 'Column', 'Frame'], as_index=False).std()

means_columns=means_frame.groupby(['Row', 'Column'], as_index=False).mean()
stds_columns=means_frame.groupby(['Row', 'Column'], as_index=False).std()

means_rows=means_columns.groupby(['Row'], as_index=False).mean()
stds_rows=means_columns.groupby(['Row'], as_index=False).std()

mi.to_csv(path_or_buf=save_dir + date + '_AntibodyResults.csv',  index=None, header=True)

means_frame.to_csv(path_or_buf=save_dir + date + '_AntibodyResults_Frame_means.csv',  index=None, header=True)
means_columns.to_csv(path_or_buf=save_dir + date + '_AntibodyResults_Column_means.csv',  index=None, header=True)
means_rows.to_csv(path_or_buf=save_dir + date + '_AntibodyResults_Row_means.csv',  index=None, header=True)

stds_frame.to_csv(path_or_buf=save_dir + date + '_AntibodyResults_Frame_stds.csv',  index=None, header=True)
stds_columns.to_csv(path_or_buf=save_dir + date + '_AntibodyResults_Column_stds.csv',  index=None, header=True)
stds_rows.to_csv(path_or_buf=save_dir + date + '_AntibodyResults_Row_stds.csv',  index=None, header=True)


print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))