from src.operations import generate_operations

def test_generate_operations(): 
    array, evens, odds = generate_operations((3,3), 0, 10) 
    assert array.shape == (3,3) 
    for i, j in evens: 
        assert array[i, j] % 2 == 0 
    for i, j in odds: 
        assert array[i,j] % 2 != 0