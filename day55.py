from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hi "
@app.route("/baye")
def baye():
    return '<h1 style="text-align:center"> fuck python</h1>' \
           '<p> this is how python fuck with my brain ' \
           '<img src="/home/kali/Pictures/scifi-astronaut-space-mars-is.jpg">'
@app.route("/<name>/<int:numbers>")
def greet(name, numbers):
    return f"<h1>hi bitch your you will  {name} your lucky number is  {numbers}</h2>"

if __name__ == "__main__":
    app.run(debug=True)