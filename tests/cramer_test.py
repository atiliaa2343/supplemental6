from src.cramer import generate_cramer 
import numpy as np 

def test_generate_cramer(): 
    coefficients = np.array([[2,-1], [1,3]]) 
    constants = np.array([1,7]) 
    solutions = generate_cramer(coefficients, constants) 
    assert np.allclose(solutions, [2,3])