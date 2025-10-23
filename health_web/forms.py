# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 16:57:08 2025

@author: USER
"""
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

#建立表單
class HealthForm(FlaskForm):
    height = FloatField("身高 (cm)", validators=[DataRequired()])
    weight = FloatField("體重 (kg)", validators=[DataRequired()])
    sleep_hours = FloatField("睡眠時間 (小時)", validators=[DataRequired()])
    exercise_minutes = FloatField("運動時間 (分鐘)", validators=[DataRequired()])
    hba1c = FloatField("糖化血色素 (%)", validators=[DataRequired()])
    submit = SubmitField("分析")
