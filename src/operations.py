"""  
This module returns an array with the specified shape of integers and 
return the indexes of all even numbers and odd numbers as separate lists and the array. 

Functions: 
generate_operations: generates array, even list, and odd list
"""

import numpy as np 

def generate_operations(shape, low, high): 
    """ 
    Returns an array of integers, even numbers, and odd numbers

    Parameters: 
    shape: A tuple defining the dimensions of the array. 
    low: The lower bound of the random integers. 
    high: The upper bound of the random integers.

    Returns: 
    list: Three separate lists: even numbers, odd numbers, and all integers

    """
    array = np.random.randint(low, high + 1, size=shape) 
    even_indexes = np.argwhere(array % 2 == 0).tolist() 
    odd_indexes = np.argwhere(array % 2 != 0).tolist() 
    return array, even_indexes, odd_indexes