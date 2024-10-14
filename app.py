from flask import Flask
import os

app = Flask(__name__)
env_var = os.getenv('ENV_VAR')

@app.route('/')
def hello_world():
    return f'<h1>Environment Variable : {env_var}</h1>'

if __name__ == '__main__':
    app.run()
