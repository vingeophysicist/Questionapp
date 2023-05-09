import random
import string



alphanumeric_character = string.ascii_lowercase + string.digits
string_length = 7

def generate_string(chars=alphanumeric_character, length=string_length):
    return "".join(random.choice(chars) for _ in range(length))


