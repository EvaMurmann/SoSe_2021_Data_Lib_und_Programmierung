# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 09:50:11 2021

@author: alpha
"""

from flask import Flask, render_template, request

print(__name__)
app = Flask (__name__)

#Decorator 
@app.route("/") #Start page 
def start_page():
    return "<p>Hello World!</p>"

@app.route("/info") #Information page
def show_info():
    return "<p>Some information</p>"

@app.route("/isbn/<isbn>") #
def isbn_display(isbn):
    return render_template ("isbn_display.html", isbn=isbn)


@app.route("/isbn_form")
def isbn_form():
    return render_template ("isbn_form.html")

@app.route("/isbn_form_content", methods=["GET"])
def isbn_form_display():
    isbn = request.args.get("isbn")
    print(request.args)
    return render_template ("isbn_display.html", isbn=isbn)