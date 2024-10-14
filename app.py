from flask import Flask
import os

app = Flask(__name__)
env_var = os.getenv('ENV_VAR')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
