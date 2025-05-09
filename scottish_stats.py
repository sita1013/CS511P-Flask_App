from models import get_all_deployments
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    rows = get_all_deployments()
    return render_template('index.html', rows = rows)