from flask import Flask, json, request
from main import euclidean_distance, knn, mode, mean

api = Flask(__name__)

@api.route('/api/knn', methods=['POST'])
def get_result():
    data = json.loads(request.data)
    reg_query = [data['query']]
    reg_k_nearest_neighbors, reg_prediction = knn(
        data['dataset'], reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean
    )
    return json.dumps(reg_k_nearest_neighbors)

if __name__ == '__main__':
    api.run(debug=True)