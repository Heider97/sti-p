from datetime import datetime
from main import euclidean_distance, knn, mean

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))



# Create a handler for our read (GET) people
def main(dataset, reg):
    #validate the for to push the correct columns into array
    clf_data = []
    data = []
    index = 1
    for key in dataset:
        data.append(key)
        if index%2 == 0:
            clf_data.append(data)
            data = []
        index = index + 1

    reg_query = [reg]
    reg_k_nearest_neighbors, reg_prediction = knn(
        clf_data, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean
    )
    return reg_k_nearest_neighbors;
