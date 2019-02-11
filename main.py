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
    if x.count('@') >= 1:
        return True
    else:
        return False

def multiple_at_signs(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def a_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def multiple_periods(x):
    if x.count('.') <=1:
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
    email = request.form['email']

    #error messages

    username_error = ""
    password_error = ""
    password_validation_error = ""
    email_error = ""
    spaces_error = "Entry cannot contain spaces."
    required_error = "This field is required."
    length_error = "Entry must be between 3 and 20 characters."
    reenter_error = "Please re-enter your password."

    #username validation
    #reset password fields for security
    #keep email and username fields

    if not empty_field(username):
        username_error = required_error
        password = ''
        password_validation = ''
        password_error = reenter_error
        password_validation_error = reenter_error
    elif not right_length(username):
        username_error = length_error
        password = ''
        password_validation = ''
        password_error = reenter_error
        password_validation_error = reenter_error
    else:
        if " " in username:
            username_error = spaces_error
            password = ''
            password_validation = ''
            password_error = reenter_error
            password_validation_error = reenter_error

    #email validation

    if empty_field(email):
        if not right_length(email):
            email_error = length_error
            password = ''
            password_validation = ''
            password_error = reenter_error
            password_validation_error = reenter_error
        elif not valid_email(email):
            email_error = "Email must contain an @ symbol."
            password = ''
            password_validation = ''
            password_error = reenter_error
            password_validation_error = reenter_error
        elif not multiple_at_signs(email):
            email_error = "Email must contain only one @ symbol."
            password = ''
            password_validation = ''
            password_error = reenter_error
            password_validation_error = reenter_error
        elif not a_period(email):
            email_error = "Email must contain a ."
            password = ''
            password_validation = ''
            password_error = reenter_error
            password_validation_error = reenter_error
        elif not multiple_periods(email):
            email_error = "Email must contain only one ."
            password = ''
            password_validation = ''
            password_error = reenter_error
            password_validation_error = reenter_error
        else:
            if " " in email:
                email_error = spaces_error
                password = ''
                password_validation = ''
                password_error = reenter_error
                password_validation_error = reenter_error
                

    #password validation

    if not empty_field(password):
        password_error = required_error
        password =  ''
        password_validation = ''
    elif not right_length(password):
        password_error = length_error
        password = ''
        password_validation = ''
        password_validation_error = reenter_error
    else:
        if " " in password:
            password_error = spaces_error
            password = ''
            password_validation = ''
            password_validation_error = reenter_error

    #second password entry

    if password_validation != password:
        password_validation_error = "Your passwords must match."
        password = ''
        password_validation = ''
        password_error = 'Your passwords must match.'

#Show welcome page for valid input
#Otherwise, remain on same page

    if not email_error and not username_error and not password_error and not password_validation_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('main.html', email_error=email_error, email=email, username_error=username_error, username=username, password_error=password_error, password=password, password_validation_error=password_validation_error, password_validation=password_validation)

# Redirect to the welcome page

@app.route('/welcome')
def signup_success():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()




