from nose.tools import assert_equal

from mod import fib

def test_fib0():
    # test edge 0
    obs = fib(0)
    assert_equal(1, obs)

def test_fib1():
    # test edge 1
    obs = fib(1)
    assert_equal(1, obs)

def test_fib6():
    # test regular point
    obs = fib(6)
    assert_equal(13, obs)
