import pytest

def prework():
    print("prework")

def postwork():
    print("postwork")

@pytest.fixture(scope="function")
def setup():
    prework()

def test_initial_check(setup):
    print("test_initial_check")
