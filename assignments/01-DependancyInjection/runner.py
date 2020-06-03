"""
Run this file to test your bomb diffuser.
"""

import bomb
import builtins
import io
import sys

from contextlib import redirect_stdout
from uuid import uuid4

for key in sys.modules:
    if key not in ["_io", "re", "bomb"]:
        sys.modules[key] = None

bomb.secret_code = str(uuid4())

f = io.StringIO()
with redirect_stdout(f):
    import submission

if bomb.secret_code not in f.getvalue():
    print("Did not print secret code.")
    exit(1)
if 'BOOOOOOOM' in f.getvalue():
    print("Bomb went off!")
    exit(1)
print("All checks passed!")
exit(0)