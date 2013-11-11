'''package exam_o_matic
A few things needed by modules in this package.

@version: $Id: __init__.py 329 2010-10-12 14:50:32Z sander $
@author: Peter Sander
'''
import sys

archive_types = ('.gz', '.jar', '.tgz', '.zip')
encoding = 'UTF-8'
findbugs_home = '/opt/software/findbugs/lib'
findbugs_path = '/opt/software/findbugs/bin'
sys.path.append(findbugs_path)
javac = '/usr/bin/javac'
java = '/usr/bin/java'
jar = '/usr/bin/jar'
jdom_path = '/usr/share/java/jdom1.jar'
junit_path = '/usr/share/java/junit4.jar'