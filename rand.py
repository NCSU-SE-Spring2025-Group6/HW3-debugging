import secrets
# import subprocess

def random_array(arr):
    for i in range(len(arr)):
        # shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True)
        # arr[i] = int(shuffled_num.stdout)
        # Utilizing Python's built-in secrets module to 
        # generate cryptographically secure random numbers
        # Generate a random number between 1 and 20
        shuffled_num = secrets.randbelow(20) + 1  
        arr[i] = shuffled_num
    return arr
