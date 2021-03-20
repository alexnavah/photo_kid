from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
<html> 
    <head> 
      <title>Simple App</title> 
     </head> 
      <body> 
        <h1>Hello</h1> 
        <p>From Flask - no templates</p> 
      </body> 
</html>'''