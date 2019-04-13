import pandas as pd
import numpy as np
from geopy.distance import great_circle

def euclidian(xf, hs):
    distance = (great_circle(tuple(xf), tuple(hs)).miles)

    return distance    #in miles


def giveHosp():
    df = pd.read_csv('Hospitals.csv')

    col_keep = ["X", "Y", "NAME", "ADDRESS", "STATE", "CITY"]

    df = df[col_keep]

    md = []

    xfinity = [-76.9414, 38.9953]


    for index, row in df.iterrows():
        if row['STATE'] == "MD":
            temp = [row['X'], row['Y']]
            euc = euclidian(xfinity, temp)
            #print(row['NAME'],euc)
            if euc < 50:
                md.append(row)

    ret = []
    j = 0
    for m in md:
        temp = []
        for i in range(0, len(col_keep)):
            temp.append(m[i])
        ret.append(temp)
    return ret

# print(giveHosp())

def giveEMS():
    df = pd.read_csv('Emergency_Medical_Service_EMS_Stations.csv')

    col_keep = ["X", "Y", "NAME", "ADDRESS", "STATE", "CITY"]

    df = df[col_keep]

    md = []

    xfinity = [-76.9414, 38.9953]


    for index, row in df.iterrows():
        if row['STATE'] == "MD":
            temp = [row['X'], row['Y']]
            euc = euclidian(xfinity, temp)
            if euc < 3:
                md.append(row)

    return md
