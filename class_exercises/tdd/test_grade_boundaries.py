import pytest
from class_exercises.tdd.grade_boundaries import calc_grade

test_data_min = [(0,"U"),
             (61,"E"),
             (105,"D"),
             (150,"C"),
             (195,"B"),
             (240,"A"),
             (299,"A*"),
             ]

test_data_max = [(60,"U"),
             (104,"E"),
             (149,"D"),
             (194,"C"),
             (239,"B"),
             (298,"A"),
             (350,"A*"),
             ]

@pytest.mark.parametrize("score, grade", test_data_min)
def test_calc_grade_min_boundary(score, grade):
    assert calc_grade(score) == grade

@pytest.mark.parametrize("score, grade", test_data_max)
def test_calc_grade_max_boundary(score, grade):
    assert calc_grade(score) == grade

def test_calc_grade_invalid():
    with pytest.raises(ValueError):
        calc_grade(400)
    with pytest.raises(ValueError):
        calc_grade(-9)
    with pytest.raises(TypeError):
        calc_grade("A")
    with pytest.raises(TypeError):
        calc_grade(8.6)

def test_calc_grade():
    assert calc_grade(259) == "A"
    assert calc_grade(188) == "C"