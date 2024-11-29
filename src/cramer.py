""" 
This module provides mathematical operations for systems of equations. 

Functions: 
    generate_cramer: Solve a system of linear equations using Cramer's rule.
"""

import numpy as np 

def generate_cramer(mat, constant): 
    """ 
    Solve a system of linear equations using Cramer's rule.

    Parameters: 
    mat : A square matrix of coefficients. 
    constant: A 1D array of constants with length n. 

    Returns: 
    list: A list of solutions to the system of equations. 

    Raises: 
        ValueError: If the determinant of the coefficient matrix is zero, indicating that the system has no unique solution.

    """
    D = np.linalg.det(mat) 

    if D == 0: 
        raise ValueError("The system of equations has no solution") 
    
    num_vars = mat.shape[1] 
    solutions = [] 

    for i in range(num_vars): 
        modified_mat = mat.copy() 
        modified_mat[:, i] = constant 
        Di = np.linalg.det(modified_mat)
        solutions.append(Di / D) 
    return solutions