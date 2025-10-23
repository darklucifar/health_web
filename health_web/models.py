# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 16:54:38 2025

@author: USER

建立資料庫模型
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    sleep_hours = db.Column(db.Float)
    exercise_minutes = db.Column(db.Float)
    hba1c = db.Column(db.Float)
    prediction = db.Column(db.Float)


