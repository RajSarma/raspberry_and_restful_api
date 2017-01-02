
from flask import Flask, request, flash, url_for, redirect, render_template


app = Flask(__name__)

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)

@app.route('/new', methods = ['GET', 'POST'])
def new():
	if request.method == 'POST':
		t =int(request.form['delay1'])
		if t>0:
			if request.form['status']=='OFF':
				GPIO.output(18,GPIO.LOW)
			else:
				while True:
					GPIO.output(18,GPIO.HIGH)
					time.sleep(t)
					GPIO.output(18,GPIO.LOW)
					time.sleep(t)
			return redirect(url_for('new'))
	return render_template('new.html')

if __name__ == '__main__':
	app.run(debug = True)
