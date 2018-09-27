from app import app
from app.forms import searchForm
from app.controller import query
import pandas as pd
from flask import render_template, Flask, redirect, request

@app.route('/', methods=['GET', 'POST'])
def homePage():
        
    form = searchForm(request.form)
    QueryObj = query()
    
    if request.method == 'POST' and form.validate_on_submit():
        
        fname,  mname,  lname = form.firstName.data, form.middleName.data, form.lastName.data
        print(fname,  mname,  lname)

        pdata = QueryObj.queryterm(fname, mname,  lname)

        return render_template('home.html', form = form, data=pdata.to_html())

    return render_template('home.html', form = form)
    