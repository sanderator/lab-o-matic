#! /usr/bin/env python
'''
Automagically analyzes a student code submission, eg, an assignment.

@author: sander
'''

import lab_o_matic.dearchiver
import lab_o_matic.compiler
#import lab_o_matic.findbugs
import lab_o_matic.runner
#import lab_o_matic.check_for_stuff

#from lab_o_matic import exam_default

#_archive_file_type = 'tar'
#_bytecode_path_defaults = ['/bin', '/build/classes']
#_decryption_key_default = '1827640192877364539209487126355121984'
#_exam_default = '/examenPOO_'
#_exam_default = ''


def main(paths, runnable_classes, optionals, unit_tests):
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
            if runnable_classes:
                lab_o_matic.runner.run_classes(paths, runnable_classes)
#            if optionals['findbugs']:
#                lab_o_matic.findbugs.findbugs(paths)
#            if optionals['check_for_stuff']:
#                lab_o_matic.check_for_stuff.check_for_stuff(paths)
#            if len(unit_tests):
#                lab_o_matic.runner.runner(unit_tests)
    

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
#    parser.add_option('-a', '--apps_path', dest='apps_path', help='directory containing student application archive directories')
#    parser.add_option('-c', '--check_for_stuff', action='store_true', dest='check_for_stuff',
#                      default=False, help='set to check for code features')
#    parser.add_option('-f', '--findbugs', action='store_true', dest='findbugs', default=False, help='run findbugs on code')
#    parser.add_option('-K', '--key', dest='decryption_key', default=_decryption_key_default, help='decryption key')
    parser.add_option('-p', '--projects', dest='projects', help='directory containing student project directories')
    parser.add_option('-r', '--run', dest='runnable_classes', default='', help='list of classes to run')
    parser.add_option('-s', '--student', dest='student', help='student name')
#    parser.add_option('-t', '--type_archive', dest='archive_type', default=_archive_file_type, help='archive file type')
#    parser.add_option('-u', '--unit_tests', dest='unit_tests', default='', help='list of unit tests to run')
    (options, args) = parser.parse_args()
    optionals = {}
#    optionals['check_for_stuff'] = options.check_for_stuff
#    optionals['findbugs'] = options.findbugs
    runnable_classes = []
    if len(options.runnable_classes):
        runnable_classes = options.runnable_classes.split()
    paths = {}
    paths['projects'] = options.projects
    paths['student'] = options.student
    unit_tests = []
#    if len(options.unit_tests):
#        unit_tests = options.unit_tests.split()
    main(paths, runnable_classes, optionals, unit_tests)
