import pickle
import json
import numpy as np

__area_type = None
__location = None
__data_column = None
__model = None


def get_estimated_price(location, sqft, bhk, bath, area=None):
    global area_index
    try:
        loc_index = __data_column.index(location.lower())
        if area is not None:
            area_index = __data_column.index(area.lower())
            print(area, area_index)
    except:
        loc_index = -1
        area_index = -1
    x = np.zeros(len(__data_column))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    if area:
        if area_index >= 0:
            x[area_index] = 1
    return round(__model.predict([x])[0], 2)


def get_location_names():
    return __location


def get_area_types():
    return __area_type


def load_saved_artifacts():
    print("Loading artifacts start...")
    global __data_column
    global __location
    global __model
    global __area_type

    with open("artifacts/column_info.json", "r") as f:
        __data_column = json.load(f)["data_columns"]
        __location = __data_column[3:-3]
        __area_type = __data_column[-3:]

    with open("artifacts/bangalore_home_price.pickle", "rb") as f:
        __model = pickle.load(f)

    print("Loading artifacts done...")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st phase jp nagar", 1000, 3, 3, "carpet  area"))
    print(get_estimated_price("1st phase jp nagar", 1000, 2, 2, "carpet  area"))
    print(get_estimated_price("Kalhalli", 1000, 2, 2, ))
    print(get_estimated_price("Ejipura", 1000, 2, 2, "carpet  area"))
