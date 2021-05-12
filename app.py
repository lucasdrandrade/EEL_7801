'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


button1 = 20
button2 = 16
button1Sts = GPIO.LOW
button2Sts = GPIO.LOW
   
# Set buttons pins as an input
GPIO.setup(button1, GPIO.IN)   
GPIO.setup(button2, GPIO.IN)
	
@app.route("/")
def index():
	# Getting the Date and Time
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y | %H:%M")
	
	# Read Sensors Status
	button1Sts = GPIO.input(button1)
	button2Sts = GPIO.input(button2)
	
	templateData = {'title' : 'EEL_7801 - UFSC','time': timeString,
      'title1' : 'Este é o Status da entrada GPIO na RPI:',
      'button1'  : button1Sts,
      'button2'  : button2Sts
      }
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
