from app import app
from app import functions
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/gsm')
def gsm():
    nome_grafico_atenuacao = functions.atenuacaoEspacoLivre(900)
    nome_grafico_propagacao = functions.propagacaoEspacoLivre(900)
    return render_template("gsm.html", atenuacao=nome_grafico_atenuacao, propagacao=nome_grafico_propagacao)


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
