"""
Run this file to test your bomb diffuser.
"""

import sys
import builtins
for key in sys.modules:
    if key != "_io":
        sys.modules[key] = None
import bomb
import diffuser
