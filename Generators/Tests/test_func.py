from Generators import myfunc
import pytest


class TestClass(object):
    def test_Multiply(self):
        a=3
        b=4
        expected=12
        actual=myfunc.multiply(a,b)
        assert expected==actual

    def test_Muliply_types(self):
        with pytest.raises(TypeError):
            myfunc.multiply("aasad", "asd")
