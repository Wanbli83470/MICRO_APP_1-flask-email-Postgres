from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
import email

app = Flask(__name__)

POSTGRES_USER = "POSTGRES_USER"
POSTGRES_PW = "POSTGRES_PW%"
POSTGRES_URL = "POSTGRES_URL"
POSTGRES_DB = "POSTGRES_DB"

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__="data"
	id=db.Column(db.Integer, primary_key=True)
	email_=db.Column(db.String(120), unique=True)
	height_=db.Column(db.Integer)

	def __init__(self, email_, height_):
		self.email_= email_
		self.height_ = height_

@app.route("/")
def index():
	condition = 0
	return render_template("index.html", condition = condition)



@app.route("/success", methods=['POST'])
def success():
	condition = 0
	if request.method == 'POST':
		print("method post")
		email=request.form['email_name']
		height=request.form['height_name']
		print(f"Votre adresse email est : {email}, vous mesurez : {height} cm")
		exist = email
		condition = 0
		if db.session.query(Data).filter(Data.email_==email).count() == 0:
			data=Data(email, height)
			db.session.add(data)
			db.session.commit()
			print("donnée enregistrés : {} et {}".format(email, height))
			send_email(email, height)
			return render_template("success.html")
	condition = 1
	return render_template("index.html", exist=exist, condition = condition )


if __name__ == '__main__':
	app.debug=True
	app.run()
