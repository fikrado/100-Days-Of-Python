from flask import *

app = Flask(__name__)

@app.route('/')
def hellow():
    return render_template('day56.html')

app.run(debug=True )