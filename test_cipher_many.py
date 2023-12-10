from MSE import mse_cipher, mse_decipher
from main import example_sentences
from random import choice
from tools import reset


x = 100

for c in range(x):
    m = mse_cipher(choice(example_sentences), False)
    print(mse_decipher(m))

    print(f'{c} message(s) déchiffré(s)')
    reset()








