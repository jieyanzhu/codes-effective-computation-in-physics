import numpy as np
from nose.tools import assert_equal

from mod import sinc2d

def test_internal():
    exp = (2.0 / np.pi) * (-2.0 / (3.0 * np.pi))
    obs = sinc2d(np.pi / 2.0, 3.0 * np.pi / 2.0)
    assert_equal(exp, obs)

def test_edge_x():
    exp = (-2.0 / (3.0 * np.pi))
    obs = sinc2d(0.0, 3.0 * np.pi / 2.0)
    assert_equal(exp, obs)

def test_edge_x():
    exp = (2.0 / np.pi)
    obs = sinc2d(np.pi / 2.0, 0)
    assert_equal(exp, obs)

def test_corner():
    exp = 1.0
    obs = sinc2d(0.0, 0.0)
    assert_equal(exp, obs)
