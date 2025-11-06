import pytest
from class_exercises.tdd.caesar_cipher import caesar_cipher

test_data = [("hello",2,"jgnnq")
             ,("xyz",3,"abc")
             ,("hell0",2,"jgnn0")
             ,("hello",-2,"fcjjm")
             ,("abc",-3,"xyz")
             ,("HeLlO",2,"JgNnQ")
             ,("hello",100,"dahhk")
             ,("hello",-100,"lipps")
             ,(0,2,0)
             ]

@pytest.mark.parametrize("message,shift,expected", test_data)
def test(message, shift, expected):
    assert caesar_cipher(message,shift) == expected

def test_invalid():
    with pytest.raises(TypeError):
        caesar_cipher("hello","a")
    with pytest.raises(TypeError):
        caesar_cipher("hello",3.5)