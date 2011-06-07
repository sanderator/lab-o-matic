''' module findbugs.py
Runs findbugs on source code.
For more information, see http://findbugs.sourceforge.net/.

Created on Apr 13, 2011

@author: sander
'''

def findbugs(paths):
    print('Running findbugs on code in %s' % paths['bytecode'])