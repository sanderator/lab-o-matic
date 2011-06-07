'''
Created on Feb 6, 2011

@author: sander
'''

import os
import os.path
import re
import subprocess
import tarfile

from lab_o_matic import archive_types
from lab_o_matic import exam_default

def dearchive(paths):
    '''
    De-archives the first archive file found in the student submitted directory.
    '''
    result = False
#    student_dir = os.path.basename(paths['projects'] + paths['student'])
    student_dir = os.path.join(paths['projects'], paths['student'])
    for a_file in os.listdir(student_dir):
        file_ext = os.path.splitext(a_file)[1]
        print('considering %s with extension %s' % (a_file, file_ext))
        if archive_types.__contains__(file_ext):
            os.chdir(os.path.join(paths['projects'], paths['student']))  # cd to student directory
            exec('dearchive_%s("%s/%s", paths)' % (os.path.splitext(a_file)[1][1:], student_dir, a_file))
            result = os.listdir(student_dir).__contains__('src')
            if result:
                return result
    return result

def dearchive_jar(a_file, paths):
    print('de-archiving a jar file: %s' % a_file)
    subprocess.call(('/usr/bin/jar', '-xf', a_file))

def dearchive_tar(a_file, paths):
    print('de-archiving a tgz file: %s' % (a_file))
    tar_file = tarfile.open(a_file)
    tar_file.extractall()
    tar_file.close()

def dearchive_tgz(a_file, paths):
    dearchive_tar(a_file, paths)
