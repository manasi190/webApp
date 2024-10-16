from flask import Flask, render_template
import os

app = Flask(__name__)
env_var = os.getenv('ENV_VAR')

@app.route('/')
def hello_world():
    return render_template('index.html', env_var=env_var)

if __name__ == '__main__':
    app.run()
