# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 16:58:02 2025

@author: USER
"""
#分析邏輯
def analyze(data):
    score = 100
    if data['sleep_hours'] < 6:
        score -= 10
    if data['exercise_minutes'] < 30:
        score -= 10
    if data['hba1c'] > 6.5:
        score -= 20
    return max(score, 0)
