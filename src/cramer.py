import numpy as np 

def generate_cramer(mat, constant): 
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