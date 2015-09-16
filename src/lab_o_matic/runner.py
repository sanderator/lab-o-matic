'''module runner
Runs executable classes and tests.

@author: (c)2010-2015 Peter Sander
'''

import glob
import os.path
import subprocess

from lab_o_matic import java
from lab_o_matic import junit_path


def run_classes(paths, runnable_classes):
    '''
    Runs given Java classes.
    The paths argument determines where to look for bytecode .class files.
    '''
    try:
        paths['bytecode']
    except KeyError:
        paths['bytecode'] = os.path.join(
            paths['projects'], '%s/build/classes' % paths['student'])
    if os.path.exists(paths['bytecode']):
        for runnable in runnable_classes:
            print('running %s from %s' % (runnable, paths['bytecode']))
            # factoid - a successful subprocess.call returns 0
            if subprocess.call((java,
                                '-cp', '%s:%s' % (paths['bytecode'],
                                                  paths['jars']),
                                runnable)):
                print('OOPS! %s screwed up somewhere' % runnable)
    return 0  # Ok, we're being optimistic here


def run_tests(paths):
    '''
    Runs all unit tests in class classes in or below the class directory.
    '''
    testcode_dir = os.path.join(paths['projects'], paths['student']) + '/test'
    test_classes = []
    # finds class classes - presumably any Java file in the class directory
    # contains a class class
    for path in os.walk(testcode_dir):
        test_classes += glob.glob(path[0] + '/*.java')
    # massages absolute file paths into class long names
    test_classes = [path.split('/') for path in test_classes]
    test_classes = [path2long_name(path) for path in test_classes]
    print('testing  %s' % test_classes)
    subprocess.call([java,
                     '-cp', '%s:%s:%s' % (paths['bytecode'],
                                          junit_path, paths['jars']),
                     'org.junit.runner.JUnitCore'] + test_classes)


def path2long_name(path):
    '''
    Converts an absolute file path of a .java file into the class's long name.
    Assumes that the file is in a directory named 'test'.
    '''
    long_name = path[path.index('test') + 1:]
    long_name = '.'.join(long_name)
    long_name = long_name[0:long_name.index('.java')]
    return long_name
