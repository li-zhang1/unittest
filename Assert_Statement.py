import pytest
def test_InAssert():
    assert 1 == 1
def test_strAssert():
    assert "str" == "str"
def test_floatAssert():
    assert 1.0 == 1.0
def test_arrayAssert():
    assert [1, 2, 3] == [1, 2, 3]
def test_dictAssert():
    assert {"1" : 1} == {"1": 1}

#Failing unit test. to fix it, we use function approx()
# def test_floatAssert():
#     assert (0.1 + 0.2) == 0.3
from pytest import approx
def test_floatAssert():
    assert (0.1 + 0.2 ) == approx(0.3)


from pytest import raises

def raisesValueException():
    raise ValueError
def test_exception():
    with raises(ValueError):
        raisesValueException()
