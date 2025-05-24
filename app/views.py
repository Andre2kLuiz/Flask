from app import app, db
from flask import render_template, url_for, request, redirect
from app.models import Contato
from app.forms import ContatoForm

@app.route('/')
def homePage():
    usuario = 'André'
    idade = '36'

    context = {
        'usuario': usuario,
        'idade': idade,
    }
    
    return render_template('index.html', context=context)

@app.route('/contatos', methods=['GET', 'POST'])
def novapagina():
    context = {}
    if request.method == "GET":
        pesquisa = request.args.get('pesquisa')
        print('GET: ' + 'pesquisa')
        context.update({'pesquisa': pesquisa})
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        menssagem = request.form['menssagem']


        contato = Contato(
            nome=nome, 
            email=email, 
            assunto=assunto, 
            menssagem=menssagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template("contato.html", context=context)

# Recomendado
@app.route('/novo_contato', methods=['GET', 'POST'])
def novo_contato():
    form = ContatoForm() 
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homePage'))

    return render_template("contatoForms.html", context=context, form=form)

