import os
from flask import (
    Blueprint, redirect, render_template, request, url_for, g, flash
)
import psycopg2
import gspread
import readCSVs
import json
import random

bp = Blueprint('blog', __name__)

hosp = readCSVs.giveHosp()
l = len(hosp)
lat = [hosp[0][0], hosp[0][0]]
lon = [hosp[0][1], hosp[0][1]]
for h in hosp:
    if h[0] < lat[0]:
        lat[0] = h[0]
    elif h[0] > lat[1]:
        lat[1] = h[0]

    if h[1] < lon[0]:
        lon[0] = h[1]
    elif h[1] > lon[1]:
        lon[1] = h[1]

randX = random.uniform(lat[0], lat[1])
randY = random.uniform(lon[0], lon[1])

minD = 1000
minX = 0
minY = 0
for h in hosp:
    temp = [h[0], h[1]]
    dist = readCSVs.euclidian(temp, [randX, randY])
    if dist < minD:
        minD = dist
        minX = h[0]
        minY = h[1]

# print(minX, minY)

@bp.route('/medical_history')
def medical_history():
    return render_template('medical_history.html')

# @bp.route('/results')
# def results():
#     return render_template('results.html')

@bp.route('/vitals')
def vitals():
    return render_template('vitals.html')

@bp.route('/attached')
def attached():
    return render_template('attached.html', lat=randY, lon=randX, minX=minX, minY=minY)

@bp.route('/locations')
def arc():
    return render_template('locations.html', hosp=json.dumps(hosp), l=l, lat=randY, lon=randX)

@bp.route('/biometrics')
def biometrics():
    return render_template('ml.html')

@bp.route('/')
def index():
    return render_template('index.html')
