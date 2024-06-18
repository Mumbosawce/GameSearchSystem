from flask import Flask

app = Flask('content')

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"