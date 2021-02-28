# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:07:06 2021

@author: Arnab
"""

import requests 
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"\Content-Type": "application/json", charset=UTF-8}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()