
from mlib import gfile
import pytest
import os


def test_basename_without_ext_01():
    path = '/home/user/project/data.jpg'
    assert gfile.basename_without_ext(path) == 'data'


def test_basename_without_ext_02():
    path = '/home/user/project/data.tar.gz'
    assert gfile.basename_without_ext(path) == 'data'


def test_basename_without_ext_03():
    path = '/home/user/project/data'
    assert gfile.basename_without_ext(path) == 'data'


def test_basename_without_ext_04():
    with pytest.raises(ValueError):
        path = '/home/user/project/data.ext.ext.ext'
        gfile.basename_without_ext(path)


@pytest.fixture
def filepath():
    with open('numbers.txt', 'w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield 'numbers.txt'

    os.remove('numbers.txt')


def test_load_numbers_sorted(filepath):
    assert gfile.load_numbers_sorted(filepath) == [1, 2, 3, 4, 5]
