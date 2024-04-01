import pandas as pd
import numpy as np
data ={"Name":["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Emily Davis",
             "Michael Wilson", "Sarah Clark", "David Martinez", "Jennifer Taylor", "James Anderson",
             "Jessica White", "William Thomas", "Elizabeth Lee", "Christopher Harris", "Karen Allen",
             "Matthew Wright", "Laura Turner", "Daniel Walker", "Rebecca Hall", "Andrew Baker"],
       "Age":[30, 35, 40, 45, 28, 32, 36, 38, 27, 42, 29, 37, 31, 43, 26, 41, 33, 39, 34, 44],
       "Salary":[60000, 62000, 58000, 65000, 55000, 59000, 63000, 64000, 56000, 67000,
               56000, 64000, 57000, 68000, 54000, 66000, 57000, 65000, 58000, 69000]   
}
df = pd.DataFrame(data)
print(df)

import pandas as pd
df = pd.read_csv("C:/Users/anshi/Desktop/DataSets/2015_16_Statewise_Elementary.csv")
print(df)
print(df.info())
df.describe()
print(df.isnull().sum())

# identify and remove duplicate values

import pandas as pd
df = pd.read_csv("C:/Users/anshi/Desktop/DataSets/2015_16_Statewise_Elementary.csv")
print(df)

if df["STATNAME"].duplicated().any():
    print(" Sum of duplicate values:",df["STATNAME"].duplicated().sum())
    df = df.drop_duplicates("STATNAME")
print(df)

# working with missing data

import pandas as pd
df = pd.read_csv("C:/Users/anshi/Desktop/DataSets/2015_16_Statewise_Elementary.csv")

dis=df["DISTRICTS"].mean();
vil=df["VILLAGES"] .mean();
tot=df["TOTPOPULAT"].mean();
gro=df["GROWTHRATE"].mean();

if df.isnull().sum().any()>0:
    df["DISTRICTS"] = df["DISTRICTS"].replace(np.nan,dis)
    df["VILLAGES"] = df["VILLAGES"].replace(np.nan,vil)
    df["TOTPOPULAT"] = df["TOTPOPULAT"].replace(np.nan,tot)
    df["GROWTHRATE"] = df["GROWTHRATE"].replace(np.nan,gro)

if df["STATNAME"].duplicated().any():
#     print(" Sum of duplicate values:",df["STATNAME"].duplicated().sum())
    df = df.drop_duplicates("STATNAME")
print(df)
