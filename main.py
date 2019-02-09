from flask import Flask, request, redirect, render_template

import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True 

#to show form

@app.route('/signup')
def user_signup_form():
    return render_template('main.html')

#trigger an error if the following

#the user leaves a field empty

#the name/pass are not valid (<3,>20)

#pass & confirmation don't match

#not a valid email (single @, single ., no space, >3, <20 )

#feedback message next to field it refers to

#preserve what user wrote for username and email

#clear password fields for security

#Show welcome page for valid input

