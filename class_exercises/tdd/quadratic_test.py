import pytest
from class_exercises.tdd.quadratic import quadratic

test_data = [(1,1,0,"0.0,-1.0")
             ,(1,0,-1,"1.0,-1.0")
             ,(1,-2,-3,"3.0,-1.0")

             ]

@pytest.mark.parametrize("a,b,c,answer", test_data)
def test(a, b, c, answer):
    assert quadratic(a, b, c) == answer

def test_invalid():
    with pytest.raises(ValueError):
        quadratic(0,0,0)
    with pytest.raises(TypeError):
        quadratic(("a",-2,-3))
    with pytest.raises(TypeError):
        quadratic((1, "a", -3))
    with pytest.raises(TypeError):
        quadratic((1,-2,"a"))