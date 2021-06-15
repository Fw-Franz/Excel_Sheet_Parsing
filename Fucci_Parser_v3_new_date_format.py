import numpy as np
import seaborn as sns
import pandas as pd
import time
import os

start_time = time.time()
base_directory =  os.getcwd() + '\\'

#region Input parameters
# input_dir_base="C:\\Users\\evolo\\OneDrive\\Juanita\\Fucci_analysis\\Parse_CellProfiler_Scripts\\INPUT\\" # do not include the date-subfolder here, that will be pulled automatically
input_dir_base = base_directory + "INPUT\\"
save_dir=input_dir_base # you can just write this as << save_dir = input_dir_base  >> if you want to save it in the same base directory as the input files, otherweise specify other directory
date='05_25_2021' # sth like '01_21_2021'

frame_n=2 # 1, 2, or ... total number of frames
plate_n=3 # total number of plates
well_n=60 # total number of wells

#endregion

input_fname_rfp="MyExpt_RFP_obj.csv"
input_fname_yfp="MyExpt_YFP_obj.csv"
input_fname_rfp_yfp="MyExpt_RFP_YFP.csv"

def parse_fucci_group(mi, df, plate, well, unique_Days, marker):
    for day in unique_Days:
        dfi = df[(df.Metadata_Plate == plate) & (df.Metadata_Timepoint == well) & (df.Metadata_Day == day)]
        fucci_i = len(dfi.index)
        new_row_i = {'PlateNum': plate, 'WellNum': well, 'DayNum': day, 'Count': fucci_i, 'Marker': marker}
        mi = mi.append(new_row_i, ignore_index=True)
    return mi

for frame in range(1, frame_n+1):
    print('----------------------------------------')
    print('processing frame ', frame)
    print('----------------------------------------')

    print('loading data ... ')
    df_rfp=pd.read_csv(input_dir_base+date+'M'+str(frame)+'\\'+input_fname_rfp)
    df_yfp=pd.read_csv(input_dir_base+date+'M'+str(frame)+'\\'+input_fname_yfp)
    df_rfp_yfp=pd.read_csv(input_dir_base+date+'M'+str(frame)+'\\'+input_fname_rfp_yfp)

    mi = pd.DataFrame(data=None, index=None, columns=['PlateNum', 'WellNum', 'DayNum', 'Count', 'Marker'])

    Days_list = df_rfp['Metadata_Day'].to_numpy()
    unique_Days = np.unique(Days_list)
    print('Days_List: ', unique_Days)

    for plate in range(1, plate_n+1):
        print('-------------------')
        print('processing plate ', plate)
        print('-------------------')

        for well in range(1, well_n+1):
            print('processing well:', well)

            mi = parse_fucci_group(mi, df_rfp, plate, well, unique_Days, 0)
            mi = parse_fucci_group(mi, df_yfp, plate, well, unique_Days, 1)
            mi = parse_fucci_group(mi, df_rfp_yfp, plate, well, unique_Days, 2)

    mi.to_csv(path_or_buf=save_dir + date + 'M' +str(frame) + 'FucciResultsCounts.csv',  index=None, header=None)


print("\n time spent in minutes: %s" % round(((time.time() - start_time))/60, 1))