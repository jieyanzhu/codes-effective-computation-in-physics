from nose.tools import assert_equal

from mod import c

def test_c():
   exp = 6
   obs = c(2)
   assert_equal(exp, obs)
