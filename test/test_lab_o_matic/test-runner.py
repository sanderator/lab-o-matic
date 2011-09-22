'''
Created on Jun 14, 2011

@author: sander
'''

from tools import with_setup, raises, nottest

import lab_o_matic.runner

_tests = ['dome.v4.CDTest']

def setup_func():
    pass

def teardown_func():
    pass

@not
@with_setup(setup_func, teardown_func)
def test_runner():
    lab_o_matic.runner.runner(_tests)