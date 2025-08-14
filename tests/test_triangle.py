from mygeopy.triangle import hypot
import numbers

def test_hypot():
    assert hypot(3, 4) == 5
    assert hypot(5, 12) == 13
    assert hypot(8, 15) == 17
    assert hypot(0, 0) == 0
    assert hypot(1, 1) == (2**0.5)
    assert hypot(1+1j,1-1j) == 2, "death by complex numbers"
    print("All tests passed!")
