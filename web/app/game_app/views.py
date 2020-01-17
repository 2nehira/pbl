from flask import request, redirect, url_for, render_template, flash
from game_app import app, db
from game_app.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result')
def rank():
    user = User.query.order_by(User.score).all()
    return render_template('result.html', users=user)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    score = request.form['score']
    user = User(
            name = request.form['name'],
            score = request.form['score']
            )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('rank'))