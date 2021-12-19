import os

from nose.tools import assert_equal, with_setup

from mod import f

def f_setup():
    files = os.listdir('.')
    if 'no.txt' in files:
        os.remove('no.txt')
    if 'yes.txt' in files:
        os.remove('yes.txt')

def f_teardown():
    files = os.listdir('.')
    if 'yes.txt' in files:
        os.remove('yes.txt')

@with_setup(setup=f_setup, teardown=f_teardown)
def test_f():
    exp = 42
    f()
    with open('yes.txt', 'r') as fhandle:
        obs = int(fhandle.read())
    assert_equal(exp, obs)
