
from flask import Blueprint, render_template, request,flash, url_for, redirect
#from .models import Build


components = Blueprint('components', __name__)

@components.route('/components')
def complexComponents():
    return render_template('components.html')
