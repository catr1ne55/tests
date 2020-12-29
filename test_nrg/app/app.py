from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return 'The app is up and running'


@app.route('/get_data', methods=['GET'])
def get_info():
    id = request.args.get('id')
    if not id:
        return 'Please, provide the id!'
    else:
        id = int(id)
        row = data[data['id'] == id]
        start_value = row['0']
        if start_value != 0:
            end_value = row['364']
            cagr_value = cagr(start_value, end_value, 1)
        else:
            return 'Please, choose another id! Zero division!!!'
    return jsonify({'CAGR': float(cagr_value)})


def cagr(start_value, end_value, period):
    return ((end_value / start_value) ** (1 / period)) - 1


if __name__ == '__main__':
    data = pd.read_csv('dataset.csv')
    app.run(debug=False, host='0.0.0.0', port=5000)
