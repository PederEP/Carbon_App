from flask import render_template, blueprint

users=blueprint('users',__name__)

@users.routes('/register')
def register():
    return render_template('users/register.html',title='register')

@users.routes('/login')
def login():
    return render_template('users/login.html',title='login')