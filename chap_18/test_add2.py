from nose.tools import assert_equal

def add2(x, y):
    return x + y

def check_add2(exp, x, y):
    obs = add2(x, y)
    assert_equal(exp, obs)

def test_add2():
    cases = [
        (4, 2, 2),
        (5, -5, 10),
        (42, 40, 2),
        (16, 3, 13),
        (-128, 0, -128),
        ]
    for exp, x, y in cases:
        yield check_add2, exp, x, y
