
from contextlib import redirect_stdout
from assert_called import verify_called_count
import io

f = io.StringIO()

with redirect_stdout(f):
    from my_file import restricted_function, main

verify_called_count("restricted_function", 1)
if "SECRETCODE" not in f.getvalue():
    print(
        "Error: importing my_file should call restricted "
        "function and print the secret"
    )
    exit(1)


f = io.StringIO()

with redirect_stdout(f):
    restricted_function()

verify_called_count("restricted_function", 2)
if "SECRETCODE" in f.getvalue():
    print(
        "Error: calling restricted_function from other_file"
        " should not print the secret code"
    )
    exit(1)


f = io.StringIO()

with redirect_stdout(f):
    main()

verify_called_count("restricted_function", 3)
if "SECRETCODE" not in f.getvalue():
    print(
        "Error: calling main from other_file"
        " should print the secret code"
    )
    exit(1)

print("All Tests Passed!!")
