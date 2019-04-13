import os
from flask import (
    Blueprint, redirect, render_template, request, url_for, g, flash
)
import psycopg2
import gspread
import readCSVs
import json


bp = Blueprint('blog', __name__)

@bp.route('/locations')
def arc():
    hosp = readCSVs.giveHosp()
    l = len(hosp)
    print(hosp)
    return render_template('locations.html', hosp=json.dumps(hosp), l=l)

@bp.route('/user_EMT')
def user():
    return render_template('user.html')

@bp.route('/biometrics')
def biometrics():
    return render_template('ml.html')

@bp.route('/')
def index():
    return render_template('index.html')
