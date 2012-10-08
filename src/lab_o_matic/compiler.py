'''module compiler.py
Compiles Java code.

author: (c)2010 Peter Sander
'''

import glob, os, subprocess, sys

from lab_o_matic import java
from lab_o_matic import javac
from lab_o_matic import junit_path

def clean(bytecode):
    '''
    Cleans up all compiled bytecode as well as compiler-generated subdirectories.
    '''
    import shutil
    shutil.rmtree(bytecode)

def compile(paths, encoding):
    '''
    Compiles any .java files it finds.
    The paths argument determines where to look for source files and
    where to put generated bytecode .class files.
    '''
    sourcecode_dir = os.path.join(paths['projects'], paths['student'])
    try:
        paths['bytecode']
    except KeyError:
        paths['bytecode'] = os.path.join(paths['projects'], '%s/build/classes' % paths['student'])
    if not os.path.exists(paths['bytecode']):
        os.makedirs(paths['bytecode'])
    files = []
    # compiles source code
    for path in os.walk(sourcecode_dir):
        files += glob.glob(path[0] + '/*.java')
    print('compiling java source code %s into %s' % (files, paths['bytecode']))
    return not subprocess.call([javac, '-encoding', encoding, '-d', paths['bytecode'], '-cp', paths['bytecode'] + ':' + junit_path] + files)