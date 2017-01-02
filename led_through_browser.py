from flask import Flask, request, flash, url_for, redirect, render_template


app = Flask(__name__)

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if  request.form['status']=="ON":
        GPIO.setup(18,GPIO.OUT)
        print "LED on"
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
      else:
        print "LED off"
        GPIO.output(18,GPIO.LOW)
        return redirect(url_for('new'))
   return render_template('new.html')

if __name__ == '__main__':
   app.run(debug = True)

