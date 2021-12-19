from nose.tools import assert_equal

def kepler_loc(p1, p2, dt, t):
    ...
    return p3

def test_kepler_loc():
    p1 = jupiter(two_days_ago)
    p2 = jupiter(yesterday)
    exp = jupiter(today)
    obs = kepler_loc(p1, p2, 1, 1)
    assert_equal(exp, obs)

# In general, the test function follows the following pattern
# def test_func():
#     exp = get_expected()
#     obs = func(*args, **kwargs)
#     assert exp == obs
