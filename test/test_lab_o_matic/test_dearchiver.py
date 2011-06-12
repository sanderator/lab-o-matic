'''
Created on May 8, 2011

@author: sander
'''

import os.path
import shutil
import sys

'''
nose.tools has to be imported into the Eclipse project, eg, from
/usr/local/lib/python2.6/dist-packages/nose-1.0.0-py2.6.egg/nose/tools.py
'''
from tools import with_setup, raises, nottest

import lab_o_matic.dearchiver

paths = {}

def setup_func():
    '''Creates fixtures.
    Note that nose doesn't work properly if this function is just called setup.
    '''
    paths['projects'] = os.path.join(os.path.dirname(__file__), '../data')

def teardown_func():
    '''Removes fixtures.
    Note that nose doesn't work properly if this function is just called teardown.
    '''
    shutil.rmtree(os.path.join(paths['projects'], paths['student'] + '/src'))
    
@with_setup(setup_func, teardown_func)
def test_dearchive_jar():
    '''
    Checks that a jar archive file is de-archived into the student directory.
    '''
    paths['student']= 'stoodent_jar'
    result = lab_o_matic.dearchiver.dearchive(paths)
    assert result
    assert os.path.exists(os.path.join(paths['projects'], paths['student'] + '/src'))
    
@with_setup(setup_func, teardown_func)
def test_dearchive_tgz():
    '''
    Checks that a tgz archive file is de-archived into the student directory.
    '''
    paths['student']= 'stoodent_tgz'
    result = lab_o_matic.dearchiver.dearchive(paths)
    assert result
    assert os.path.exists(os.path.join(paths['projects'], paths['student'] + '/src'))
    
@raises(OSError)
def test_unknown_stoodent():
    paths['student']= 'stoodent_foo'
    lab_o_matic.dearchiver.dearchive(paths)
