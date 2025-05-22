from app import app
from flask import render_template, url_for

@app.route('/')
def homePage():
    usuario = 'André'
    idade = '36'

    context = {
        'usuario': usuario,
        'idade': idade,
    }
    
    return render_template('index.html', context=context)

@app.route('/contatos')
def novapagina():
    return "outra view"

