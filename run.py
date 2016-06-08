import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # import pdb; pdb.set_trace()
    i = 3
    return "Hello everyone!\nYou visited %d times" % i
    

if __name__=='__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run( host=host, port=port)
