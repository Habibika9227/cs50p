
from hello import hello

def test_hello():
    assert hello("Abdalla")=="hello,Abdalla"
    assert hello()=="hello,world"

test_hello()
