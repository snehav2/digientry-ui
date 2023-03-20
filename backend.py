from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
def main():
    return render_template('sign-up.html')

class User(db.Model):
    registration_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    branch= db.Column(db.String(40))
    room_no = db.Column(db.Integer(10))
    year= db.Column(db.Integer(10))
    password= db.Column(db.Integer(20))
    confirm_password=db.Column(db.Interger(20))


    def __init__(self, registration_number,name,branch,room_no,year, password,confirm_password):
        self.name=name
        self.registration_number = registration_number
        self.branch=branch
        self.room_no=room_no
        self.year=year
        self.password=password
        self.confirm_password =confirm_password

@app.route('/sign-up.html', methods=['POST'])
def sign-up():
    registration_number=request.form['Registration No.']
    name = request.form['Name']
    branch=request.form['Branch']
    room_no=request.form['Room No.']
    year=request.form['Year']
    password=request.form['Password']
    confirm_password=request.form['Confirm Password']
    new_user = User(registration_number,name,branch,room_no,year,password,confirm_password)
    db.session.add(new_user)
    db.session.commit()

    return 'User added successfully!'

if __name__ == '__main__':
    app.run(debug=True)
