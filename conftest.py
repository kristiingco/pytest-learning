import pytest 

def prework():
    print("prework")

def postwork():
    print("postwork")

@pytest.fixture(scope="function")
def setup():
    prework()
    return True

@pytest.fixture(scope="function")
def post_test():
    postwork()
    return True