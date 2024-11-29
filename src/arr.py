import numpy as np 

def generate_array(shape, mean, std_dev): 
    """ 
    Finds the specified shape array of normally distributed numbers with a given mean and standard deviation 

    Parameters: 
    shape: Defines the dimensions of the array to be generated 

    mean: The mean of the normal distribution 

    std_dev: The standard deviation of the normal distribution

    Returns 
    An array of random numbers with the specified shape, mean, and std_dev


    
    
    """
    return np.random.normal(loc=mean, scale=std_dev, size=shape)