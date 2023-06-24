from flask import *

from werkzeug.utils import secure_filename
import os
import csv

app=Flask(__name__)
app.secret_key="dont tell"

@app.route("/")
def index():
 return render_template('reg.html')


@app.route("/register",methods=['GET','POST'])
def register():
		
		return render_template("fbform.html")

@app.route("/feedback")
def feedback():
		
		return redirect(url_for('userfeedback'))

@app.route("/userfeedback")
def userfeedback():
		rollno=10
		
		
		return render_template("userfeedback.html",rollno=rollno)

@app.route("/feedbackpage",methods=['GET','POST'])
def feedbackpage():
		
		
		
		return redirect(url_for('feedback'))

@app.route("/viewfeedback",methods=['GET','POST'])
def viewfeedback():	
	
		
		course="department"
		data = ["disease1","disease2","disease3"]
		
		
		
		
		percentage="56%"
		
		
		return render_template("viewfeedback.html",data=data,percentage=percentage,course=course)	


if __name__=="__main__":
	app.run(debug=True)
