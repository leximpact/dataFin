
import json
from flask import Flask, render_template
from flask_cors import CORS

from back.dotation_solidarite_rurale import eligible_dsr


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    # source : https://leafletjs.com/examples/quick-start/
    return render_template('index.html')


@app.route('/communes_polygons')
def communes_polygons():
    with open('./back/inputs/communes-20190101.json') as json_file:
        data = json.load(json_file)
    print(data.keys())
    return json.dumps(data['features'])

@app.route('/dotations/dsr/eligebilite', methods=['GET', 'POST'])
def communes_eligibles():
    return {
        "communes": {
            "eligibles": 6000,
            "nouvelles": 11,
            "anciennes": 4,
        }
    }


if __name__ == '__main__':
   app.run(debug=True)
   
