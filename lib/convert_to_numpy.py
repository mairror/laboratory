import numpy as np
import ast

def convert_to_np_array(array):
    if array != np.nan:
        arr = ast.literal_eval(array)
        return np.array(arr)