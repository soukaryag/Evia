import pandas as pd
import numpy as np
# from geopy.distance import great_circle
import math

def euclidian(xf, hs):
    # distance = (great_circle(tuple(xf), tuple(hs)).miles)
    R = 6372800  # Earth radius in meters
    lat1 = xf[0]
    lon1 = xf[1]
    lon2 = hs[1]
    lat2 = hs[0]

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2

    distance = 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a)) /1000
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
            if euc < 50:
                md.append(row)

    return md
