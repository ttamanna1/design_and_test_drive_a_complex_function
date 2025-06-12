from lib.age_checker import *
import pytest

def test_age_above_sixteen():
    result = age_checker("1960-10-21")
    assert result == 'Access granted'

def test_age_below_sixteen():
    result = age_checker("2015-10-21")
    assert result == 'Access denied. Your age is 9. You need to be 16.'

def test_date_is_str():
    with pytest.raises(Exception) as e:
        age_checker(12/10/1999)
    assert str(e.value) == 'Enter DOB in string format.'

def test_if_date_in_correct_format():
    with pytest.raises(Exception) as e:
        age_checker("67632897")
    assert str(e.value) == 'Enter DOB in string format: YYYY-MM-DD.'
    
    