# get_ipython().getoutput("pip install pandas-profiling==2.6")


import os
import pandas as pd
from pandas_profiling import ProfileReport


# set up directory
os.chdir('/Volumes/GoogleDrive/My Drive/508/Project_508/Data/')
data_sets = os.listdir()
data_sets


for data_set in data_sets:
    df = pd.read_parquet(data_set)

    # get data name
    data_name = data_set.split('.')[0]
    
    # compile Pandas Profile report
    print(f'Building {data_name} report.')
    ProfileReport(df).to_file(f"{data_name}_report.html")
    
    print('--'*30,)
print('get_ipython().getoutput("!'*10, '----', 'Profiling Complete','-----','!!'*10)")



