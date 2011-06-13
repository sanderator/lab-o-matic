'''
Created on Feb 6, 2011

@author: sander
'''

import os.path
import subprocess

def check_for(sourcecode_dir, whatever, lines=5):
    subprocess.call(('/usr/bin/rgrep', '-C', str(lines), '-h', whatever, sourcecode_dir))
    
def check_for_stuff(paths):
    sourcecode_dir = os.path.join(paths['projects'], paths['student'])
    print('\n\n\t**********checking for author**********')
    check_for(sourcecode_dir, '@author', 1)
    print('\n\n\t**********checking for constants**********')
    check_for(sourcecode_dir, '"static final"\|"final static"')
    print('\n\n\t**********checking for enum**********')
    check_for(sourcecode_dir, 'public enum')
    print('\n\n\t**********checking for abstract class or interface and inheritance**********')
    check_for(sourcecode_dir, 'abstract\|interface\|extends\|implements')
    print('\n\n\t**********checking for HashMap or Map**********')
    check_for(sourcecode_dir, 'HashMap\|Map')
    print('\n\n\t**********checking for try-catch**********')
    check_for(sourcecode_dir, 'catch')
    print('\n\n\t**********checking for singleton Data**********')
    check_for(sourcecode_dir, 'static\|"private Data"', 10)