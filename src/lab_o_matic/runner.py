'''module runner
Runs executable classes and tests.

@author: (c)2010 Peter Sander
'''

import os.path
import subprocess

def run_classes(paths, runnable_classes):
    '''
    Runs given Java classes.
    The paths argument determines where to look for bytecode .class files.
    '''
#    try:
#        paths['bytecode']
#    except KeyError:
#        paths['bytecode'] = os.path.join(paths['projects'], '%s/build/classes' % paths['student'])
    if os.path.exists(paths['bytecode']):
        for runnable in runnable_classes:
            print('running %s from %s' % (runnable, paths['bytecode']))
            # factoid - a successful subprocess.call returns 0
            if subprocess.call(('/usr/bin/java', '-cp', paths['bytecode'], runnable)):
                print('OOPS! %s screwed up somewhere' % runnable)
    return 0  # Ok, we're being optimistic here

def runner(tests):
    '''
    Runs given unit tests.
    '''
    print('running tests: %s' % tests)
    subprocess.call('/usr/local/bin/nosetests', '--nocapture', os.path.join(os.path.dirname(__file__), '../../test'))