import numpy as np
from src.arr import generate_array
def test_generate_array(): 
    """ 
    Tests the function to ensure it creates an array with the specified shape, mean, and standard deviation 

    The test performs the following checks: 
    1. Validates that the generated array has the correct shape 
    2. Confirms that the mean of the generated array is close to the specified mean 
    3. Confirms that the standard deviation of the array is close to the specified standard deviation
    
    Parameters: 
    None 

    Returns: 
    None
    
    """
    array = generate_array((2,3), mean=0, std_dev = 1) 
    assert array.shape == (2,3) 
    assert np.isclose(array.mean(), 0, atol=1) 
    assert np.isclose(array.std(), 1, atol=1)