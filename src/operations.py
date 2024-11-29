import numpy as np 

def generate_operations(shape, low, high): 
    array = np.random.randint(low, high + 1, size=shape) 
    even_indexes = np.argwhere(array % 2 == 0).tolist() 
    odd_indexes = np.argwhere(array % 2 != 0).tolist() 
    return array, even_indexes, odd_indexes