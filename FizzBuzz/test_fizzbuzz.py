import pytest

#Green phase
#Production code.
def fizzBuzz(value):
    if isMultiple(value,3):
        if isMultiple(value,5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value,5):
        return 'Buzz'
    return str(value)

#From specific to general.
def isMultiple(value, mod):
    return (value % mod) == 0

def checkFizzBuzz(value, expectedRes):
    res = fizzBuzz(value)
    assert res == expectedRes

#1.Red phase. 
# def test_cancallFizzBuzz():
#     fizzBuzz(1)

#2.Red phase.
def test_returns1With1PassedIn():
    checkFizzBuzz(2,"2")
    # res = fizzBuzz(1)
    # assert res == "1"
#3. Red Phase.
def test_returns2With2PassedIn():
    checkFizzBuzz(1, "1")
    # res = fizzBuzz(2)
    # assert res == "2"

# Red Phase.
def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

# Red Phase.
def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5,"Buzz")

# Red Phase.
def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6,"Fizz")

# Red Phase.
def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

# Red Phase.
def test_returnsFizzBuzzwith15PassedIn():
    checkFizzBuzz(15,"FizzBuzz")

#Test Driven Development(TDD):
#Red Phase (write failing test code)
#Green Phase (write production code to pass the test)
#Refactor Phase (see if code needed to refatored.)

#Output -> Python Test Log

