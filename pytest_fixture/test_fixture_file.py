import pytest
@pytest.fixture(autouse = True)
def setup():
    print("\nSetup")
def test1():
    print("Executing test1!")
    assert True

#@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2!")
    assert True

#pytest -v -s