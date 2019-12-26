
from assert_called import assert_called

SECRET_CODE = "SECRETCODE"

@assert_called("restricted_function")
def restricted_function():
    pass # fill this out


def main():
    restricted_function()


restricted_function()