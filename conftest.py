import pytest 

def prework():
    print("prework")

def postwork():
    print("postwork")
    
@pytest.fixture(scope="function")
def setup():
    prework()
