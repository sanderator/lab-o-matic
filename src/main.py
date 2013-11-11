#! /usr/bin/env python3
'''
Automagically analyzes a student code submission, eg, an assignment.

@author: sander
'''

import lab_o_matic.dearchiver
from lab_o_matic.diagram import diagram
import lab_o_matic.compiler
from lab_o_matic import encoding
from lab_o_matic.findbugs import findbugs
import lab_o_matic.runner
#import lab_o_matic.check_for_stuff


def main(paths, runnable_classes, optionals, unit_tests):
    '''
    De-archives submitted copy, compiles application and JUnit tests.
    Runs findbugs static code analyzer. Runs JUnit tests.
    '''
    # to de-archive or not to de-archive
    if not optionals['dearchive'] or lab_o_matic.dearchiver.dearchive(paths):
        # de-archived ok, let's compile the source code
        if lab_o_matic.compiler.compile(paths, optionals['encoding']):
            # compiled ok, let's do unnatural things to it
            if optionals['diagram']:
                diagram(paths)
            if optionals['findbugs']:
                findbugs(paths)
            # either runs application or runs unit tests on application
            if runnable_classes:
                lab_o_matic.runner.run_classes(paths, runnable_classes)
#            if optionals['check_for_stuff']:
#                lab_o_matic.check_for_stuff.check_for_stuff(paths)
#            if len(unit_tests):
            else:
                lab_o_matic.runner.run_tests(paths, unit_tests)
    

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
#    parser.add_option('-c', '--check_for_stuff', action='store_true', dest='check_for_stuff',
#                      default=False, help='set to check for code features')
    parser.add_option('-d', '--diagram', action='store_true', dest='diagram', default=False, help='create and display UML class diagram')
    parser.add_option('-e', '--encoding', dest='encoding', default=encoding, help='source file character encoding (you probably want ISO8859-1)')
    parser.add_option('-f', '--findbugs', action='store_true', dest='findbugs', default=False, help='run findbugs on code')
    parser.add_option('--no-dearchive', action='store_false', dest='dearchive', default=True, help='do not de-archive student project')
    parser.add_option('-p', '--projects', dest='projects', help='directory containing student project directories')
    parser.add_option('-r', '--run', dest='runnable_classes', default='', help='list of classes to run')
    parser.add_option('-s', '--student', dest='student', help='student name')
#    parser.add_option('-t', '--type_archive', dest='archive_type', default=_archive_file_type, help='archive file type')
    parser.add_option('-u', '--unit_tests', dest='unit_tests', default='', help='list of unit tests to run')
    (options, args) = parser.parse_args()
    optionals = {}
#    optionals['check_for_stuff'] = options.check_for_stuff
    optionals['diagram'] = options.diagram
    optionals['encoding'] = options.encoding
    optionals['findbugs'] = options.findbugs
    optionals['dearchive'] = options.dearchive
    runnable_classes = []
    if len(options.runnable_classes):
        runnable_classes = options.runnable_classes.split()
    paths = {}
    paths['projects'] = options.projects
    paths['student'] = options.student
    unit_tests = []
    if len(options.unit_tests):
        unit_tests = options.unit_tests.split()
    main(paths, runnable_classes, optionals, unit_tests)
