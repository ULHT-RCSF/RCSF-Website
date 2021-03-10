from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/gsm')
def gsm():
    return render_template('gsm.html')


@app.route('/gsm-r')
def gsmr():
    return render_template('gsm-r.html')


@app.route('/umts')
def umts():
    return render_template('umts.html')


@app.route('/lte')
def lte():
    return render_template('lte.html')

@app.route('/cincog')
def cincog():
    return render_template('cincog.html')


@app.route('/wi_fi')
def wi_fi():
    return render_template('wi_fi.html')


@app.route('/cloud_ran')
def cloud_ran():
    return render_template('cloud-ran.html')


@app.route("/sobre")
def sobre():
    return render_template('sobre.html')
