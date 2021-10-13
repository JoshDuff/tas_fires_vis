import pandas as pd
import os

os.chdir("C:/Users/duffj/Desktop/FIT3179/Project2/tas_fires_vis")
file_handle = pd.read_csv("data/tas_fires_long.csv")

dictionary = {}

for i, row in file_handle.iterrows():
    if i > 3250:
        break
    incd_num = row["INCD_NO"]
    year = row["Year"]
    if incd_num not in dictionary:
        dictionary[incd_num] = 41*[None]
        dictionary[incd_num][int(year - 1980)] = row["IGN_CAUSE1"]
    else:
        dictionary[incd_num][int(year - 1980)] = row["IGN_CAUSE1"]

dict_frame = pd.DataFrame.from_dict(dictionary).T
dict_frame.to_csv("data/tas_fires_wide.csv")