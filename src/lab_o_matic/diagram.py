''' module diagram.py
Creates and displays a UML class diagram.

@author: (c)2013-2015 Peter Sander
'''

import os
import shutil
import subprocess

from lab_o_matic import dot
from lab_o_matic import doxygen
from lab_o_matic import doxygen_config
from lab_o_matic import doxygraph_home
from lab_o_matic import okular
from lab_o_matic import perl


def diagram(paths):
    print('Generating UML class diagram')
    wd = os.getcwd()
    student_dir = os.path.join(paths['projects'], paths['student'])
    os.chdir(student_dir)
    print('deoxygening in %s' % os.getcwd())
    # doxygen generates documentation for the code
    subprocess.call((doxygen, doxygen_config))
    print('deoxygraphing in %s' % os.getcwd())
    # doxygraph turns XML into DOT format
    # must be run from the doxygraph home directory
    os.chdir(doxygraph_home)
    graph_dot = os.path.join(student_dir, 'graph.dot')
    subprocess.call((perl, 'doxygraph/doxygraph',
                     os.path.join(student_dir,
                                  'xml/index.xml'), graph_dot))
    # and dot converts dot file to pdf
    subprocess.call((dot, '-T', 'pdf',
                     '-o', os.path.join(student_dir, 'UML.pdf'), graph_dot))
    # cleans up after itself
    shutil.rmtree(os.path.join(student_dir, 'xml'))
    os.remove(os.path.join(student_dir, 'graph.dot'))
    subprocess.call((okular, os.path.join(student_dir, 'UML.pdf')))
    os.chdir(wd)
