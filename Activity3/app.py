from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
return """

@app.route('/')
def greet():
  username = request.args.get('username', 'World')
  favefood = request.args['favefood']
  if favefood == '':
    msg = 'You did nit tell me your favorite food.'
else:
  msg = 'I like' + favefood + ', too.'
  
return """
<html><body>
<h2>Hello, {0}!</h2>
 {1}
</body></html>
""".format(username, msg)


app.run(host="localhost", debug=True)
