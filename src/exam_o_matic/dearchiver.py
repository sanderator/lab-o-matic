'''
Created on Feb 6, 2011

@author: sander
'''

import os.path
import tarfile

def dearchive(paths):
    '''
    Dearchives submitted file.
    '''
    result = False
    student = os.path.basename(paths['student'])
    exam_file = paths['student'] + '/examenPOO_' + student + '.tgz'
    if os.path.isfile(exam_file):
        print('dearchiving exam file: %s' % (exam_file))
        tar_file = tarfile.open(exam_file, 'r:gz')
#        tar_file.list()
        tar_file.extractall(paths['student'])
        tar_file.close()
        if os.path.exists(paths['student'] + '/examenPOO_' + student):
            # everything probably dearchived ok
            result = True
    else:
        print('cannot find exam file: %s' % exam_file)
    return result
