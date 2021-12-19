from nose.tools import assert_equal

from mod2 import std

def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert_equal(exp, obs)

def test_std2():
    obs = std([])
    exp = 0.0
    assert_equal(exp, obs)

def test_std3():
    obs = std([0.0, 4.0])
    exp = 2.0
    assert_equal(exp, obs)

def test_std4():
    obs = std([1.0, 3.0])
    exp = 1.0
    assert_equal(exp, obs)

def test_std5():
    obs = std([1.0, 1.0, 1.0])
    exp = 0.0
    assert_equal(exp, obs)
