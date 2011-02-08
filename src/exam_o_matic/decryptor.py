'''
Created on Feb 6, 2011

Decrypts student exam submission file.

author: (c)2011 Peter Sander
'''

import os.path
import subprocess

def decrypt(paths, decryption_key):
    '''
    Decrypts submitted file.
    '''
    result = False
    student = os.path.basename(paths['student'])
    exam_file = paths['student'] + '/examenPOO_' + student + '.tgz.cpt'
    if os.path.isfile(exam_file):
        print('decrypting exam file: %s' % (exam_file))
        result = subprocess.call(('/usr/bin/ccrypt', '-f' '-d', '-K', decryption_key, exam_file))
        if not result:
            print('decryption ok')
            result = True
    else:
        print('cannot find exam file: %s' % exam_file)
    return result