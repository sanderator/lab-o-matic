''' module findbugs.py
Runs findbugs on source code.
For more information, see http://findbugs.sourceforge.net/.

Created on Apr 13, 2011

@author: sander
'''

import os.path
import subprocess

from lab_o_matic import java
from lab_o_matic import findbugs_home


def findbugs(paths):
    print('Running findbugs on code in %s' % paths['bytecode'])
    findbugs_output = os.path.join(paths['projects'], '%s/findbugs.fb' % (paths['student']))
    return not subprocess.call((java, '-jar', '%s/findbugs.jar' % (findbugs_home),
                                '-textui', '-output', findbugs_output, paths['bytecode']))
