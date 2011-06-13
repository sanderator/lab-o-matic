''' module findbugs.py
Runs findbugs on source code.
For more information, see http://findbugs.sourceforge.net/.

Created on Apr 13, 2011

@author: sander
'''

import os.path
import subprocess

_findbugs_home = '/opt/software/findbugs/lib'

def findbugs(paths):
    print('Running findbugs on code in %s' % paths['bytecode'])
    try:
        paths['findbugs_home']
    except KeyError:
        paths['findbugs_home'] = _findbugs_home
    try:
        paths['findbugs_output']
    except KeyError:
        findbugs_output = os.path.join(paths['projects'], '%s/findbugs.fb' % (paths['student']))
        paths['findbugs_output'] = findbugs_output
            
    return not subprocess.call(('/usr/bin/java', '-jar', '%s/findbugs.jar' % (paths['findbugs_home']),
                                '-textui', '-output', paths['findbugs_output'], paths['bytecode']))

