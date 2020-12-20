from flask import render_template, redirect, request
import re   





# Home Page
def landing():
    return render_template("index.html")
#About page
def about_page():
    return render_template("about.html")
#Packages page
def packages_page():
    return render_template("packages.html")



