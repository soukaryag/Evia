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
ems = readCSVs.giveEMS()
l = len(hosp)
l2 = len(ems)
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

@bp.route('/vitals_arms')
def vitals_arms():
    return render_template('vitals_arms.html')

@bp.route('/vitals_chest')
def vitals_chest():
    return render_template('vitals_chest.html')

@bp.route('/vitals_torso')
def vitals_torso():
    return render_template('vitals_torso.html')

@bp.route('/vitals_legs')
def vitals_legs():
    return render_template('vitals_legs.html')

@bp.route('/vitals_shoulder')
def vitals_shoulder():
    return render_template('vitals_shoulder.html')

@bp.route('/vitals_head')
def vitals_head():
    return render_template('vitals_head.html')

@bp.route('/medical_history')
def medical_history():
    return render_template('medical_history.html')

@bp.route('/med')
def med():
    return render_template('med.html')

@bp.route('/pat_info')
def pat_info():
    return render_template('pat_info.html')

@bp.route('/vitals')
def vitals():
    return render_template('vitals.html')

@bp.route('/attached')
def attached():
    return render_template('attached.html', lat=randY, lon=randX, minX=minX, minY=minY)

@bp.route('/locations_found')
def locations_found():
    return render_template('locations_found.html', hosp=json.dumps(hosp), ems=json.dumps(ems), l=l, l2=l2, lat=randY, lon=randX)

@bp.route('/locations')
def arc():
    t = random.randint(4,8)
    return render_template('locations.html', hosp=json.dumps(hosp), ems=json.dumps(ems), l=l, l2=l2, lat=randY, lon=randX, time=t)

@bp.route('/biometrics')
def biometrics():
    return render_template('ml.html')

@bp.route('/')
def index():
    return render_template('index.html')
