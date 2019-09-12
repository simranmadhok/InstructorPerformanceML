#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:54:19 2019

@author: simranmadhok
"""
import numpy as np
import pandas as pd

MIN_AVG_SCORE = 3

student_scores = pd.read_csv(r"C:\Users\Simran\Desktop\Anaconda Projects\turkiye_student_evaluation.csv")
print("----------INITIAL STUDENT SCORE-------")
print(student_scores)
local = np.array(student_scores)
Satisfactory = []

for row in local:
    if np.mean(row[5:]) >= MIN_AVG_SCORE:
        Satisfactory.append(1)
    else:
        Satisfactory.append(0)

student_scores['PERFORMANCE'] = Satisfactory
print("----------DATA PRE-PROCESSED STUDENT SCORE-------")
print(student_scores)

student_scores.to_csv(r'C:\Users\Simran\Desktop\Anaconda Projects\final_dataset.csv')
