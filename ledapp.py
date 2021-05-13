'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
import datetime
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define the buttons GPIO pin
button1 = 20
button2 = 16

#initialize GPIO status variales (buttons)
button1Sts = GPIO.LOW
button2Sts = GPIO.LOW


# Set button and PIR sensor pins as an input
GPIO.setup(button1, GPIO.IN)   
GPIO.setup(button2, GPIO.IN)

#define actuators GPIOs
ledRed = 13
ledGrn = 19
ledYlw = 26

#initialize GPIO status variables (variables)
ledRedSts = 0
ledYlwSts = 0
ledGrnSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledYlw, GPIO.OUT) 
GPIO.setup(ledGrn, GPIO.OUT) 

# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYlw, GPIO.LOW)
GPIO.output(ledGrn, GPIO.LOW)
	
@app.route("/")
def index():
	
	# Read Sensors Status
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)
	
	# Getting the Date and Time
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y | %H:%M")
	
	# Read Sensors Status
	button1Sts = GPIO.input(button1)
	button2Sts = GPIO.input(button2)

	templateData = {'title' : 'EEL_7801 - UFSC','time': timeString,
              'title1' : 'GPIO output Status!',
	      'button1'  : button1Sts,
	      'button2'  : button2Sts,
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts,
              'ledGrn'  : ledGrnSts,
        }
	
	return render_template('index2.html', **templateData)
	
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	if deviceName == 'ledYlw':
		actuator = ledYlw
	if deviceName == 'ledGrn':
		actuator = ledGrn
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
	ledYlwSts = GPIO.input(ledYlw)
	ledGrnSts = GPIO.input(ledGrn)
	
	# Getting the Date and Time
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y | %H:%M")
	
	# Read Sensors Status
	button1Sts = GPIO.input(button1)
	button2Sts = GPIO.input(button2)
   
	templateData = {'title' : 'EEL_7801 - UFSC','time': timeString,
              'title1' : 'Os botões físicos representam entradas externas de sinal. O leds são ativados pelos botões virtuais da página.',
	      'button1'  : button1Sts,
	      'button2'  : button2Sts,
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts,
              'ledGrn'  : ledGrnSts,
	}
	
	return render_template('index2.html', **templateData)
	
if __name__ == "__main__":
   app.run(debug=True)
