#!C:\Users\xcpro\ve0\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nose==1.0.0','console_scripts','nosetests-2.7'
__requires__ = 'nose==1.0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('nose==1.0.0', 'console_scripts', 'nosetests-2.7')()
    )