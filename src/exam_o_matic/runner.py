'''module runner
Runs tests.

@version: $Id: runner.py 329 2010-10-12 14:50:32Z sander $
@author: (c)2010 Peter Sander
'''

import sys

from org.junit.runner import JUnitCore

def runner(tests):
    print('running tests: %s' % tests)
    JUnitCore.main(tests)