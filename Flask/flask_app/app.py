from flask import Flask
'''  
It creates an instance of the flask class,  
which will be your WSGI(Web Server Gateway Interface) application.  
'''  
##wsgi application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "<html><body><h1 style='color:green;'>THIS IS THE UPDATED VERSION</h1></body></html>"

if __name__=="__main__":
    app.run(debug=True)
