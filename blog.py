import os
from flask import (
    Blueprint, redirect, render_template, request, url_for, g, flash
)
import psycopg2
import gspread

bp = Blueprint('blog', __name__)

@bp.route('/locations')
def arc():
    return render_template('locations.html')

@bp.route('/user_EMT')
def user():
    return render_template('user.html')

@bp.route('/biometrics')
def biometrics():
    return render_template('ml.html')

@bp.route('/')
def index():
    return render_template('index.html')
