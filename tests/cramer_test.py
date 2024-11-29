from src.cramer import generate_cramer 
import numpy as np 

def test_generate_cramer(): 
    """ 
    Test the generate_cramer function to ensure it correctly solves linear equations using Cramer's rule. 

    The test performs the following checks: 
    1. Defines a coefficient matrix and a constants vector for a system of equations. 
    2. Passes the inputs to the function
    3. Ensures that the computed solutions match the expected values
    """
    coefficients = np.array([[2,-1], [1,3]]) 
    constants = np.array([1,7]) 
    solutions = generate_cramer(coefficients, constants) 
    assert np.allclose(solutions, [2,3])