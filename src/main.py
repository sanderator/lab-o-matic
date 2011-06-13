#! /usr/bin/env jython
'''
Automagically analyzes a student code submission, eg, an assignment.

@author: sander
'''

import lab_o_matic.dearchiver
import lab_o_matic.compiler
import lab_o_matic.findbugs
import lab_o_matic.runner
import lab_o_matic.check_for_stuff

from lab_o_matic import exam_default

_archive_file_type = 'tar'
_bytecode_path_default = '/build/classes'
_decryption_key_default = '1827640192877364539209487126355121984'
#_exam_default = '/examenPOO_'
#_exam_default = ''

def main(decryption_key, paths, tests, check_for_stuff, findbugs=False):
    '''
    Decrypts submitted copy, compiles application and tests; runs tests.
    '''
#    result = lab_o_matic.decryptor.decrypt(paths, decryption_key)
#    if True:
        # de-archives submission
    if lab_o_matic.dearchiver.dearchive(paths):
        # de-archived ok, let's compile the source code
        if lab_o_matic.compiler.compile(paths):
            # compiled ok, let's do unnatural things to it
            lab_o_matic.findbugs.findbugs(paths)
            lab_o_matic.check_for_stuff.check_for_stuff(paths)
    

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a', '--apps_path', dest='apps_path', help='directory containing student application archive directories')
    parser.add_option('-c', '--check_for_stuff', action='store_true', dest='check_for_stuff',
                      default=False, help='set to check for code features')
    parser.add_option('-f', '--findbugs', action='store_true', dest='findbugs', default=False, help='run findbugs on code')
    parser.add_option('-K', '--key', dest='decryption_key', default=_decryption_key_default, help='decryption key')
    parser.add_option('-p', '--projects', dest='projects', help='directory containing student project directories')
    parser.add_option('-s', '--student', dest='student', help='student name')
#    parser.add_option('-t', '--type_archive', dest='archive_type', default=_archive_file_type, help='archive file type')
#    parser.add_option('-u', '--unit_tests', dest='unit_tests', default = '', help='list of unit tests to run')
    (options, args) = parser.parse_args()
    paths = {}
    paths['projects'] = options.projects
    paths['student'] = options.student
#    paths['apps'] = paths['student'] + '/src'
#    paths['test'] = paths['student'] + '/test'
#    paths['bytecode'] = paths['student'] + _bytecode_path_default
#    sys.path.append(paths['bytecode'])
    tests = []
#    if len(options.unit_tests):
#        tests = options.unit_tests.split()
    main(options.decryption_key, paths, tests, options.check_for_stuff, options.findbugs)
