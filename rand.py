"""
Generates a random array to be used in hw2_debugging.py
Author: Autumn Wright (git: a-wright-git)(NCSU: jmwrigh3)
"""

import secrets

def random_array(arr):
    """Generates a random array of length 'arr' with values from 1-20"""
    for i,_ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
