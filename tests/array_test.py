import sys 
print(sys.path)
from src.arr import generate_array
def test_generate_array(): 
    array = generate_array((2,3), mean=0, std_dev = 1) 
    assert array.shape == (2,3) 
    assert np.isclose(array.mean(), 0, atol=1) 
    assert np.isclose(array.std(), 1, atol=1)