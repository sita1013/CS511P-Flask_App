from models import get_years_and_features, get_filtered_data
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    selected_year = request.args.get('year', type = int)
    selected_feature = request.args.get('feature')
    years, features = get_years_and_features()
    rows = get_filtered_data(selected_year, selected_feature)
    return render_template(
        'index.html', 
        rows = rows,
        years = years,
        features = features, 
        selected_year = selected_year,
        selected_feature = selected_feature

    )