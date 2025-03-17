# test_main.py
from main import add, prout 

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_prout():
    assert prout(3) == 3
    assert prout(1) == 1
    assert prout(0) == 0
