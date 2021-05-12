from flask import Flask #import the flask module 

app = Flask(__name__) #crate a flask object called

#Run the index() function when someone accesses the root URL ('/') of the server. In this case, only send the text "Hello World!" to the client's web browser thru "return"

@app.route('/')
def index():
    return 'PROJETO EM ELETRÔNICA 1'
#Once this script is running from the command line at the terminal, the server starts to "listen" on port 80, reporting any errors:
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
