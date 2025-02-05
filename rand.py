"""
Generates a random array to be used in hw2_debugging.py
Author: Autumn Wright (git: a-wright-git)(NCSU: jmwrigh3)
"""

import secrets

def random_array(arr):
    """Generates a random array of length 'arr' with values from 1-20"""
    for i,_ in enumerate(arr):
        # Utilizing Python's built-in secrets module to generate
        # cryptographically secure random numbers between 1 and 20
        # although this is not a cryptographic application
        # and this is actually not needed, random module is enough
        shuffled_num = secrets.randbelow(20) + 1
        arr[i] = shuffled_num
    return arr
