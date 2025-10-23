# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 17:00:02 2025

@author: USER
主程式
"""
from flask import Flask, render_template, redirect, url_for
from models import db, UserData
from forms import HealthForm
from ai_model import analyze

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health.db'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HealthForm()
    if form.validate_on_submit():
        data = {
            'height': form.height.data,
            'weight': form.weight.data,
            'sleep_hours': form.sleep_hours.data,
            'exercise_minutes': form.exercise_minutes.data,
            'hba1c': form.hba1c.data
        }
        prediction = analyze(data)
        entry = UserData(**data, prediction=prediction)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('index.html', form=form)

@app.route('/dashboard')
def dashboard():
    users = UserData.query.all()
    return render_template('dashboard.html', users=users)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

