
import json
from flask import Flask, render_template, request
from flask_cors import CORS

import numpy as np

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
    seuilHabitants = request.json.get('seuilHabitants')
    ponderation = request.json.get('ponderation')
    eligibilite_par_code_insee = eligible_dsr(max_nombre_habitants = seuilHabitants, ponderation = ponderation)
    indexes_communes_eligibles = np.where(eligibilite_par_code_insee == True)[0]

    return {
        "path": "https://files.slack.com/files-tmb/TSRA44X0E-FT65P8XNJ-a708ccf600/figure_toute_bleue_720.png",
        "communes": {
            "eligibles": len(indexes_communes_eligibles),
            "nouvelles": 0,
            "anciennes": 0,
        }
    }


if __name__ == '__main__':
   app.run(debug=True)
   
