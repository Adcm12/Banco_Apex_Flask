from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
import random, re
from Models.usuario import Usuario

@app.route('/')
def login():
    return render_template('login.html', titulo='Banco Estrella Dorada')

@app.route('/micuenta')
def micuenta():
    if 'usuario_logado' in session:
        nome = session['usuario_logado']
        
        usuario = Usuario.query.filter_by(Nome=nome).first()
        if usuario:
            nome = usuario.Nome
            saldo = usuario.Saldo
            nro_c = usuario.Nro_Conta
            return render_template('cuenta.html', titulo='Banco Estrella Dorada', nomeU=nome, saldo=saldo, conta=nro_c)
    else:
        return redirect(url_for('login'))

@app.route('/registrar')
def registrar():
    return render_template('registrar.html', titulo='Banco Estrella Dorada')

@app.route('/registrar_usuario', methods=['POST'])
def registrar_usu():
    nome_usu = request.form.get('username')
    email_usu = request.form.get('email')
    senha_usu = request.form.get('password')

    numero_cuenta = random.randint(1000, 999999999)
    numero_cuenta = f"{numero_cuenta:06d}"

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    password_pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'

    existe_usuario = Usuario.query.filter_by(Nome=nome_usu).count()
    existe_email = Usuario.query.filter_by(Email=email_usu).count()

    if not re.match(email_pattern, email_usu):
        flash("Correo electrónico no válido", 'error')
        return render_template('registrar.html')

    if not re.match(password_pattern, senha_usu):
        flash("Contraseña no válida", 'error')
        return render_template('registrar.html')

    if existe_usuario > 0:
        flash("Este usuario ya está registrado", 'error')
        return render_template('registrar.html')

    if existe_email > 0:
        flash("Este email ya está registrado", 'error')
        return render_template('registrar.html')

    try:
        novo_usuario = Usuario(Nro_Conta=numero_cuenta, Nome=nome_usu, Email=email_usu, Senha=senha_usu, Saldo=0)
        db.session.add(novo_usuario)
        db.session.commit()
        flash("Registro de nuevo usuario realizado con éxito")
        return redirect(url_for('micuenta'))
    except:
        flash("Error al registrar nuevo usuario", 'error')
        return render_template('registrar.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Usuario.query.filter_by(Nome=request.form['Nome']).first()

    if usuario and request.form['password'] == usuario.Senha:
        session['usuario_logado'] = usuario.Nome
        flash(usuario.Nome + ' logado con éxito')
        return redirect(url_for('micuenta'))

    flash('Usuario o contraseña inválidos', 'error')
    return redirect(url_for('login'))
