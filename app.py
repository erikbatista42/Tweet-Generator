from flask import Flask
# import cleanup
# import tokenize
import word_count
import sample
import sentence

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
