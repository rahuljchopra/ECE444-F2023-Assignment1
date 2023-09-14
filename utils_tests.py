from utils import utils

def test_reversed():
    assert utils.reversed(123) == 321
    assert utils.reversed(100) == 1

    try:
        utils.reversed("hello")
    except ValueError as e:
        assert str(e) == "Input must be an integer"

    try:
        utils.reversed("world")
    except ValueError as e:
        assert str(e) == "Input must be an integer"
    
    try:
        utils.reversed("10.5")
    except ValueError as e:
        assert str(e) == "Input must be an integer"
    
    try:
        utils.reversed("82.5")
    except ValueError as e:
        assert str(e) == "Input must be an integer"

def test_formatter():
    assert utils.formatter(123) == ("1111011", "173")
    assert utils.formatter(100) == ("1100100", "144")

    try:
        utils.formatter("hello")
    except ValueError as err:
        assert str(err) == "Input must be an integer"
    
    try:
        utils.formatter("world")
    except ValueError as err:
        assert str(err) == "Input must be an integer"
    
    try:
        utils.formatter("10.5")
    except ValueError as err:
        assert str(err) == "Input must be an integer"
    
    try:
        utils.formatter("82.5")
    except ValueError as err:
        assert str(err) == "Input must be an integer"

test_reversed()
test_formatter()
print("All tests passed.")
