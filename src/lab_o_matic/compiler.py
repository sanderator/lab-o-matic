'''module compiler.py
Compiles Java code.

author: (c)2010 Peter Sander
'''

import glob, os, subprocess, sys
#
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../test/rt.jar'))
#from javax.tools import ForwardingJavaFileManager
#
#from javax.tools import (ForwardingJavaFileManager, ToolProvider,
#         DiagnosticCollector, StandardLocation)
#from java.io import File
#
#from lab_o_matic import exam_default, jdom_path, junit_path

def clean(bytecode):
    '''
    Cleans up all compiled bytecode as well as compiler-generated subdirectories.
    '''
    import shutil
    shutil.rmtree(bytecode)

def compile(paths):
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
#    files = ' '.join(files)
    print('compiling java source code %s into %s' % (files, paths['bytecode']))
#    return subprocess.call(('/usr/bin/javac', '-d', paths['bytecode'], '`find', '"*.java"`'))
    return not subprocess.call(('/usr/bin/javac', '-d', paths['bytecode'], files[0], files[1], files[2]))