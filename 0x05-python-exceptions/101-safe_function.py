#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Function that executes a function safely.
    Args:
        fct: The function to execute.
        args: Arguments for fct.
    Return:
        If an errror occurs - None.
        Otherwise - the result of the call to fct. """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr)
        return (none)
