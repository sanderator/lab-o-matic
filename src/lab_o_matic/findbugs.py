''' module findbugs.py
Runs findbugs on source code.
For more information, see http://findbugs.sourceforge.net/.

Created on Apr 13, 2011

@author: sander
'''

import subprocess

def findbugs(paths):
    print('Running findbugs on code in %s' % paths['bytecode'])
    return not subprocess.call(('/usr/bin/java', '-jar', '%s/findbugs.jar' % (paths['findbugs_home']), 
                                '-textui', '-output', paths['findbugs_output'], paths['bytecode']))
