## HOUSES all of the html file references that are related to the website mainframe (not auth) ##
import os
from flask import (
    Blueprint, redirect, render_template, request, url_for, g, flash
)
import psycopg2
import gspread

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    return render_template('index.html')
