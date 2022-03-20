get_ipython().getoutput("pip freeze > pandas_profiling_env.txt")


# get_ipython().run_line_magic("%capture", " silences console warnings, updates, etc")
get_ipython().run_line_magic("%capture", " ")
get_ipython().getoutput("pip install pandas-profiling==2.6")


get_ipython().getoutput("pip install visions")


import pandas as pd
from pandas_profiling import ProfileReport


file_path = '/Volumes/GoogleDrive/My Drive/508/Project_508/Data/vehicle_registration.parquet.gzip'
df = pd.read_parquet(file_path)
df.shape


ProfileReport(df).to_file("vehicle_registration_report.html")


df.head()






