'''
Created on Feb 6, 2011

@author: sander
'''

import subprocess

def check_for(paths, whatever, lines=5):
    subprocess.call(('/usr/bin/rgrep', '-C', str(lines), '-h', whatever, paths['apps']))
    
def check_for_stuff(paths):
    print('\n\n\t**********checking for author**********')
    check_for(paths, '@author', 1)
    print('\n\n\t**********checking for constants**********')
    check_for(paths, '"static final"\|"final static"')
    print('\n\n\t**********checking for enum**********')
    check_for(paths, 'public enum')
    print('\n\n\t**********checking for abstract class or interface and inheritance**********')
    check_for(paths, 'abstract\|interface\|extends\|implements')
    print('\n\n\t**********checking for HashMap or Map**********')
    check_for(paths, 'HashMap\|Map')
    print('\n\n\t**********checking for try-catch**********')
    check_for(paths, 'catch')
    print('\n\n\t**********checking for singleton Data**********')
    check_for(paths, 'static\|"private Data"', 10)