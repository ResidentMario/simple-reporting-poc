# coding: utf-8
import zipfile
import requests
import io
r = requests.get("http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyc_pluto_16v1.zip")
zips = zipfile.ZipFile(io.BytesIO(r.content), 'r')

import pandas as pd
import sqlite3
conn = sqlite3.connect("mth4320.db")
for borough in ["BK", "BX", "MN", "QN", "SI"]:
    pd.read_csv("{0}.csv".format(borough)).to_sql(con=conn, name=borough)

import os
os.listdir(".")
for f in [f for f in os.listdir(".") if ".csv" in f or ".pdf" in f]:
    os.remove(f)
    
