import json
import pickle
import numpy as np

__locations=None
__datacols=None
__model=None

def get_estimated_price():
    x= np.where(__datacols==)

def get_location_names():
    print("getting location names")
    load_data()
    return __locations

def load_data():
    global __locations
    global __datacols
    
    with open('./data/columns.json', 'r') as f:
        __datacols= json.load(f)['data_columns']
        __locations=__datacols[3:]
        print("Getting x columns")

    with open('./data/home_prices_model.pickle', 'rb') as f:
        model= pickle.load(f)
        print("Loading pickle file")

if __name__ == "__main__":
    print("rRunning util")
   
    print(get_location_names())