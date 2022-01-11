from flask import (Flask, Blueprint, current_app,session,g,request, redirect, url_for,render_template)
from . import api_caller,forms
from datetime import datetime

home = Blueprint('home', __name__)

@home.route('/',methods=['POST','GET'])
def index():
    form = forms.MyForm()
    # print('starting')
    
    if form.validate_on_submit():
        # session['location'] = form.location.data
        # return redirect(url_for('forecast',location=form.location.data))
        response = api_caller.api_caller(form.location.data)
        if response.status_code != 200:
            return render_template('index.html',error='location not found',form=form)
        return redirect(url_for('forecast.forecast_location',forecast=form.location.data))
        # print('done')
        # return 'done'
        
    # print('did not validate')
    return render_template('index.html',form=form)


@home.before_app_request
def load_forecast():
    # location = session.get('location')
    default = 'london'
    g.date = datetime.now()
    # if location is None:
    #     g.forecast = api_caller.api_caller(default)
    # else:
    g.forecast = api_caller.api_caller(default).json()
    # redirect('forecast')
