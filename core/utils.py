import string
import random


def generate_vid():
    S = 10
    ran = ''.join(random.choices(string.ascii_lowercase, k=S))
    print(ran)
    return ran
