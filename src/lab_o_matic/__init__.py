'''package exam_o_matic
A few things needed by modules in this package.

@version: $Id: __init__.py 329 2010-10-12 14:50:32Z sander $
@author: Peter Sander
'''
import sys

archive_types = ('.jar', '.tgz')
findbugs_path = '/opt/software/findbugs/bin'
sys.path.append(findbugs_path)
jdom_path = '/usr/share/java/jdom1.jar'
junit_path = '/usr/share/java/junit4.jar'
sys.path.append(junit_path)
sys.path.append('/usr/share/java/hamcrest-core.jar')

exam_default = ''