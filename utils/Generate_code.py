import random




def generate_code(n = 8):
    numbers = '0123456789'
    code = ''.join(random.choice(numbers) for x in range(n))
    return code

