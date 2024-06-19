from flask import render_template, redirect, url_for
from app import app, db  # Импорт переменной app и db из пакета app
from app.forms import LoginForm, RegistrationForm  # Импорт форм из app.forms

# Пример использования формы регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Обработка регистрации пользователя
        # Пример: создание нового пользователя в базе данных
        # user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        # db.session.add(user)
        # db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# Пример использования формы входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Обработка входа пользователя
        # Пример: проверка пользователя в базе данных
        # user = User.query.filter_by(email=form.email.data).first()
        # if user and check_password_hash(user.password, form.password.data):
        #     login_user(user, remember=form.remember.data)
        #     return redirect(url_for('index'))
        # else:
        #     flash('Login Unsuccessful. Please check email and password', 'danger')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)
