import secrets

def random_array(arr):
    for i in range(len(arr)):
        # Utilizing Python's built-in secrets module to generate
        # cryptographically secure random numbers between 1 and 20
        # although this is not a cryptographic application 
        # and this is actually not needed, random module is enough
        shuffled_num = secrets.randbelow(20) + 1 
        arr[i] = shuffled_num
    return arr
