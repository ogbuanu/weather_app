import functools
from flask import (Blueprint, flash, url_for, redirect, session, render_template,request,g)
from . import api_caller,forms

forecast = Blueprint('forecast', __name__, url_prefix='/forecast')


@forecast.route('/<forecast>',methods=['GET','POST'])
def forecast_location(forecast):
    form = forms.MyForm()
    response = api_caller.api_caller(forecast)
    print(response.status_code)
    if response.status_code != 200:
        error = 'location not found'
        return redirect(url_for('index',error=error))
    g.forecast = response.json()
    if form.validate_on_submit():
        response = api_caller.api_caller(form.location.data)
        if response.status_code != 200:
            error = 'location not found'
            redirect(url_for('index',error=error))
        return redirect(url_for('.forecast_location',forecast=form.location.data))
    return render_template('forecast.html',form=form)

# @forecast.before_app_request
# def forecaster():
#     location = session.get('location')
#     if location is None:
#         redirect(url_for('index'))
#     else:
#         g.forecast_data = api_caller.api_caller(location)
        

