from math import sqrt, floor
import random
import emoji

num = int(input('Digite um numero: \n'))
raiz = sqrt(num);
print("A raiz do numero {} é {}".format(num, floor(raiz)))

num2 = random.randint(1, 10)
print('numero aleatorio é {}'.format(num2))

print(emoji.emojize( 'Ola mundo :earth_americas:', use_aliases=True))