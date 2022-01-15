from main import arithm
import pytest


@pytest.fixture(scope='module')
def number():
    yield {'add': (1, 2),
           'diff': (3, 5),
           'mul': (3, 5),
           'div': (6, 3)
           }


def test_add_01(number):
    a, b = number['add']
    assert arithm.add(a, b) == 3


def test_add_02(number):
    a, b = number['add']
    assert arithm.add(b, a) == 3


def test_diff_01(number):
    a, b = number['diff']
    assert arithm.diff(a, b) == 2


def test_diff_02(number):
    a, b = number['diff']
    assert arithm.diff(b, a) == 2


def test_mul_01(number):
    a, b = number['mul']
    assert arithm.mul(a, b) == 15


def test_mul_02(number):
    a, b = number['mul']
    assert arithm.mul(b, a) == 15


def test_div_01(number):
    a, b = number['div']
    assert arithm.div(a, b) == 2


def test_div_02(number):
    a, b = number['div']
    assert arithm.div(b, a) == 0.5


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        arithm.div(1, 0)
