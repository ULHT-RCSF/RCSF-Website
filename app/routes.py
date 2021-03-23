from app import app
from app import functions
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/gsm')
def gsm():
    nome_grafico_atenuacao_900 = functions.atenuacaoEspacoLivre(900)
    nome_grafico_atenuacao_1800 = functions.atenuacaoEspacoLivre(1800)
    nome_grafico_propagacao_900 = functions.propagacaoEspacoLivre(900)
    nome_grafico_propagacao_1800 = functions.propagacaoEspacoLivre(1800)
    return render_template("gsm.html", atenuacao_900=nome_grafico_atenuacao_900, atenuacao_1800=nome_grafico_atenuacao_1800,
                           propagacao_900=nome_grafico_propagacao_900, propagacao_1800=nome_grafico_propagacao_1800)


@app.route('/gsm-r')
def gsmr():
    nome_grafico_atenuacao_880 = functions.atenuacaoEspacoLivre(880)
    nome_grafico_atenuacao_925 = functions.atenuacaoEspacoLivre(925)
    nome_grafico_propagacao_880 = functions.propagacaoEspacoLivre(880)
    nome_grafico_propagacao_925 = functions.propagacaoEspacoLivre(925)
    return render_template("gsm-r.html", atenuacao_880=nome_grafico_atenuacao_880, atenuacao_925=nome_grafico_atenuacao_925,
                           propagacao_880=nome_grafico_propagacao_880, propagacao_925=nome_grafico_propagacao_925)


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
