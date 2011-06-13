'''
Created on Jun 12, 2011

@author: sander
'''

import os, os.path
import shutil
import sys

'''
nose.tools has to be imported into the Eclipse project, eg, from
/usr/local/lib/python2.6/dist-packages/nose-1.0.0-py2.6.egg/nose/tools.py
'''

from tools import with_setup, raises, nottest

import lab_o_matic.findbugs

paths = {}
paths['findbugs_home'] = '/opt/software/findbugs/lib'
paths['findbugs_output'] = '/tmp/findbugs.fb'


def setup_func():
    '''Creates fixtures.
    Note that nose doesn't work properly if this function is just called setup.
    '''
    paths['projects'] = os.path.join(os.path.dirname(__file__), '../data')
    paths['student'] = 'stoodent_src'
    paths['bytecode'] = os.path.join(paths['projects'], '%s/build/classes' % paths['student'])
    result = lab_o_matic.compiler.compile(paths)

def teardown_func():
    '''Removes fixtures.
    Note that nose doesn't work properly if this function is just called teardown.
    '''
    shutil.rmtree(paths['bytecode'])
    os.unlink(os.path.join(paths['findbugs_output']))

@with_setup(setup_func, teardown_func)
def test_findbugs():
    assert lab_o_matic.findbugs.findbugs(paths)
    