from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

# Configurations


app = Flask(__name__, template_folder='template')

@app.route('/submit', methods=['GET', 'POST'])
def index():
    BMI = None
    status = None

    if request.method == 'POST':
        Height = float(request.form['height'])
        Weight = float(request.form['weight'])
        BMI =  round((Weight / (Height/100)**2), 1)

        if BMI < 18.5:
            status = "Underweight" 
        elif BMI >= 18.5 and BMI < 25:
            status = "Normal"
        elif BMI >= 25 and BMI < 30:
            status = "Overweight"
        elif BMI >= 30:
            status = "Obese"

    return render_template('index.html', BMI=BMI, status=status)

if __name__ == '__main__':
    app.run(debug=True)

    










