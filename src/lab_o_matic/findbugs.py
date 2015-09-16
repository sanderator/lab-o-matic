''' module findbugs.py
Runs findbugs on source code.
Findbugs output get written into a file called findbugs.fb in the student
project directory.
For more information, see http://findbugs.sourceforge.net/.

@author: (c)2013-2015 Peter Sander
'''

import os.path
import subprocess

from lab_o_matic import java
from lab_o_matic import junit_path
from lab_o_matic import findbugs_home


def findbugs(paths):
    print('Running findbugs on code in %s' % paths['bytecode'])
    findbugs_output = os.path.join(paths['projects'],
                                   '%s/findbugs.fb' % (paths['student']))
    return not subprocess.call((java,
                                '-jar', '%s/findbugs.jar' % (findbugs_home),
                                '-textui', '-output', findbugs_output,
                                '-auxclasspath', junit_path,
                                paths['bytecode']))
