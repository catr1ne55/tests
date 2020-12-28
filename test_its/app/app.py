from flask import Flask, request, jsonify
import numpy as np
import djkstra

app = Flask(__name__)


@app.route('/')
def index():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == '123321':
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


@app.route('/distance', methods=['GET'])
def get_info():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth != '123321':
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    else:
        city_start = request.args.get('city_start')
        city_finish = request.args.get('city_finish')
        g = djkstra.Graph()
        try:
            distance, path = g.dijkstra(distances, city_start, city_finish)
            if path:
                response = {
                    "body": {
                        "path": str(path),
                        "distance": str(distance)
                    }
                }
                return response
            else:
                response = {"body": "No road"}
                return jsonify(response), 401
        except Exception as e:
            response = {"body": str(e)}
            return jsonify(response), 500


if __name__ == '__main__':
    distances = np.load(open("matrix_distance", "rb"))
    distances = np.where(distances == 0, float('inf'), distances)
    app.run(debug=False, host='0.0.0.0', port=5000)
