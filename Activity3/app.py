from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
return """
<html>
<body>
<h2>Welcome to the greeter</h2>
<form action="/greet">
   What is your name? <input type='text' name='username'><br>
   What is your favorite food? <input type='text' name='favefood'><br>
   <input type='submit' value='Continue'><br>
</form>
</body>
</html>
"""

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
