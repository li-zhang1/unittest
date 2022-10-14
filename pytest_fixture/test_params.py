import pytest
@pytest.fixture(params = [1, 2, 3])
def setup(request):
    res = request.param
    print(f"\nSetup! res = {res}")
    return res
def test1(setup):
    print(f"\nsetup = {setup}")
    assert True