
# /app/controllers/auth_controller.py
from flask import render_template, redirect, url_for, session, flash
from app import app, mysql
from app.forms import RegisterForm, LoginForm, InfoForm, UserInfoForm
from app.models.user import User
from app.models.info import Info
import bcrypt

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserInfoForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Stocker les données dans la base de données
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_data (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cursor.close()

        flash("Information ajoutée avec succès !", "success")
        return redirect(url_for('index'))

    # Récupérer les informations stockées
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name, email FROM user_data ORDER BY id DESC")
    infos = cursor.fetchall()
    cursor.close()

    return render_template('index.html', form=form, infos=infos)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        User.create_user(name, email, hashed_password)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.get_user_by_email(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            flash("Login failed. Please check your email and password")
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.get_user_by_id(session['user_id'])  # Utilisez la nouvelle méthode
        if user:
            return render_template('dashboard.html', user=user)
    return redirect(url_for('login'))

    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out successfully.")
    return redirect(url_for('login'))
