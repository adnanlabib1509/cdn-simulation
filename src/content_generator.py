import random
import string

def generate_content(length=50):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))