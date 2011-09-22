'''
De-archives student submissions.

@author: sander
'''

import os.path
import subprocess
import tarfile

from lab_o_matic import archive_types

def dearchive(paths):
    '''
    De-archives the first archive file found in the student submitted directory.
    '''
    result = False
    student_dir = os.path.join(paths['projects'], paths['student'])
    # checks all files for archive type
    for a_file in os.listdir(student_dir):
        file_ext = os.path.splitext(a_file)[1]
        if archive_types.__contains__(file_ext):
            os.chdir(os.path.join(paths['projects'], paths['student']))  # cd to student directory
            dearchive_func = dearchive_dispatcher(file_ext[1:])
            result = dearchive_func(a_file, paths)
            if result:
                # no need to look any further, we have an archive file
                return result
    return result

def dearchive_jar(a_file, paths):
    '''
    De-archives a jar file.
    '''
    return not subprocess.call(('/usr/bin/jar', '-xf', a_file))  # because subprocess returns 0 on success

def dearchive_tar(a_file, paths):
    '''
    De-archives a tar file.
    '''
    tar_file = tarfile.open(a_file)
    tar_file.extractall()  # doesn't seem to return any status
    tar_file.close()
    return True  # hope that's alright

def dearchive_gz(a_file, paths):
    '''
    De-archives a gzipped tar file.
    '''
    return dearchive_tar(a_file, paths)

def dearchive_tgz(a_file, paths):
    '''
    De-archives a gzipped tar file.
    '''
    return dearchive_tar(a_file, paths)

def dearchive_dispatcher(archive_type):
    '''
    Returns the appropriate de-archiver function for the given archive type.
    '''
    return globals()['dearchive_%s' % (archive_type)]
