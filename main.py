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

def empty_field(x):
    if x:
        return True
    else:
        return False

#the name/pass are not valid (<3,>20)

def right_length(x):
    if len(x) >= 3 and len(x) <= 20:
        return True
    else:
        return False

#not a valid email (single @, single ., no space, >3, <20 )

def valid_email(x):
    if x.count('@') = 1:
        return True
    else:
        return False 

def single_period(x):
    if x.count('.') = 1:
        return True
    else:
        return False

#process form

@app.route("/signup", methods=['POST'])
def user_signup_success():

    #form input variables

    username = request.form['username']
    password = request.form['password']
    password_validation = request.form['password_validation']
    email = request.form['text']

    #error messages

    username_error = ""
    password_error = ""
    password_validation_error = ""
    email_error = ""
    spaces_error = "Entry cannot contain spaces."
    required_error = "This field is required."
    length_error = "Entry must be between 3 and 20 characters."
    reenter_error = "Please re-enter your password."

#feedback message next to field it refers to

#pass & confirmation don't match

#preserve what user wrote for username and email

#clear password fields for security

#Show welcome page for valid input

