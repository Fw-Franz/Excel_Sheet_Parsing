import pandas as pd
import numpy as np
import workspace_shelf as ws
import seaborn as sns
import matplotlib.pyplot as plt
import os, shutil

# Create shelf file to store objects in
filename=r'C:\Users\Franz\OneDrive\_PhD\Code\Test_files\Workspace.out'

shutil.copy(__file__, os.path.dirname(filename))

# Create some objects to store in shelf
string='This is a string' # a string
integer=3 # an integer
list=[1,2,3,"string"] # a list

# a pandas dataframe
# df=pd.read_csv(r'C:\Users\Franz\OneDrive\_PhD\Juanita\Spheroids\CellReporter_Data_Franz\I3C\MyExpt_Image.csv')
dataframe = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        'col2': ["a", "b", "c", "d", "e", "f", "g", "h", "i"],
                        'col3': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]})

ax=sns.lineplot(data=dataframe, x='col1',y='col2')
plt.show()

# a numpry array
# numpy_array=np.ones((1000,1000,1000)) # also works on giga arrays of 7gb
numpy_array=np.ones((10,10,10))

# load all variables into a dictionary to save using shelve
object_list=ws.save_workspace(filename,globals())
print("Object list saved:", object_list)

# delete all objects before trying to load them to see if they actually loaded (except the filename of the shelf)
for obj in object_list:
    # print(obj)
    if obj != 'filename':
        del globals()[obj]

# locals().update(ws.load_workspace(filename))
globals().update(ws.load_workspace(filename))

# print shelf obects to check
print(string)
print(integer)
print(list)
print(dataframe.size)
print(np.shape(numpy_array))