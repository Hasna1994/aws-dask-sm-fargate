import s3fs
import dask.dataframe as dd
import dask.distributed
import os
from time import ctime

s3url = os.environ['s3url']
schurl = os.environ['schurl']

print(ctime(), 'running daskclientapp.. hang tight...')


df = dd.read_csv(s3url, storage_options={'anon': True})

from dask.distributed import Client
client = Client(schurl)

print(ctime(), client.ncores())

print(ctime(), df.head())

# modify the below statement based on your s3 dataset 

dfg = df.groupby('VendorID').agg({'passenger_count':'count', 'trip_distance': 'sum'}).astype(int).reset_index().rename(columns={'passenger_count':'Trip Count'}).compute()
print(ctime(), dfg)







