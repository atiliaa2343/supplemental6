from src.operations import generate_operations

def test_generate_operations(): 
    """ 
    Test the function to ensure it: 
    1. Generates an array of integers with the specified shape
    2. Identifies the indexes of even and odd numbers 

    The test performs the following checks: 
    1. Ensures that the array has the correct shape 
    2. Confirms that the indexes of the even numbers are even
    3.. Confirms that the indexes of the odd numbers are odd
    """
    array, evens, odds = generate_operations((3,3), 0, 10) 
    assert array.shape == (3,3) 
    for i, j in evens: 
        assert array[i, j] % 2 == 0 
    for i, j in odds: 
        assert array[i,j] % 2 != 0