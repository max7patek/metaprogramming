"""
Run this file to test your bomb diffuser.
"""

import sys
import builtins
for key in sys.modules:
    sys.modules[key] = None
import bomb
import diffuser
