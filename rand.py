import random

def random_array(arr):
    for i in range(len(arr)):
        # Generate a random number between 1 and 20
        arr[i] = random.randint(1, 20)
    return arr
