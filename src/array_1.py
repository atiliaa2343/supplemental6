import numpy as np 

def generate_array(shape, mean, std_dev): 
    return np.random.normal(loc=mean, scale=std_dev, size=shape)