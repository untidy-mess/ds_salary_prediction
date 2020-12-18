# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:35:56 2020

@author: Arnab Wahid
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Arnab/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('Data Scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

