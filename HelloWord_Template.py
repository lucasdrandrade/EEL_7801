

from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route("/")
def hello():
   now = datetime.datetime.now() #Get the current time and store it in the object now
   timeString = now.strftime("%d-%m-%Y | %H:%M") #Create a formatted string using the date and time from the now object
   templateData = {'title' : 'EEL_7801-UFSC','time': timeString} #Create a dictionary of variables (a set of keys, such as title that are associated with values, such as HELLO!) to pass into the template
   return render_template('index.html', **templateData) #Return the main.html template to the web browser using the variables in the templateData dictionary
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
