from flask import Flask, render_template
import datetime

app = Flask(__name__)
@app.route("/")
def hello():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'title' : 'HELLO!',
		'time' : timeString
	}
	return render_template("main.html", **templateData)

@app.route("/getInfo/<val>")
def info(val):
	now = datetime.datetime.now()
	if(val=="time"):
		timeString = now.strftime("%H:%M")
		templateData = { 'title' : 'Time on this Pi',
			'name':'The Time is',
			'datetime': timeString}
	if(val=='date'):
		timeString = now.strftime("%Y-%m-%d")
		templateData = { 'title' : 'Date on this Pi',
			'name':'The Date is',
			'datetime':timeString}
	return render_template('date_time.html', **templateData)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
