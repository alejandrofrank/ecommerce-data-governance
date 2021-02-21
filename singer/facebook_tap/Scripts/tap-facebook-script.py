#!c:\users\aleja\desktop\alex\education\udactity\projects\capstone_project\singer\facebook_tap\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tap-facebook==1.11.0','console_scripts','tap-facebook'
__requires__ = 'tap-facebook==1.11.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tap-facebook==1.11.0', 'console_scripts', 'tap-facebook')()
    )
