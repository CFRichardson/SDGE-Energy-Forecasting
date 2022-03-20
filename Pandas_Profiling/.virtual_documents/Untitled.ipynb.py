# get_ipython().getoutput("pip install pandas-profiling==2.6")


import os
import pandas as pd
from pandas_profiling import ProfileReport


os.chdir('/Volumes/GoogleDrive/My Drive/508/Project_508/Data/')
data_sets = os.listdir()
data_sets


for data_set in data_sets:
    df = pd.read_parquet(data_set)
    
    data_name = data_set.split('.')[0]
    
    ProfileReport(df).to_file(f"{data_name}_report.html")
    
