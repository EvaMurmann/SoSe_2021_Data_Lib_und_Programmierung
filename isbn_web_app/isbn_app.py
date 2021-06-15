# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:50:11 2021

@author: alpha
"""

from flask import Flask

print(__name__)
app = Flask (__name__)

#Decorator 
@app.route("/") 
def start_page():
    return "<p>Hello World! Hope you are good!!</p>"