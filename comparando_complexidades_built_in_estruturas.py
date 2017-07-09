

import timeit
import random

#comparando tempo de execução de verificação de existência de um elemento em uma lista com o de dicionário
# length = 1000000
# l = list(range(length))
# t = timeit.Timer('random.randrange(%d) in l' % length,'from __main__ import l, random')
# print('check if element exists in list access time: ',t.timeit(number=1000))

# d = {i:None for i in range(length)}
# t = timeit.Timer('random.randrange(%d) in d' % length,'from __main__ import d, random')
# print('check if element exists in dict access time: ',t.timeit(number=1000))


# Verificar que a operação de acessar elemento de uma lista é O(1)
# length = [1000, 10000, 100000, 1000000, 10000000]
# for leng in length:
# 	l = list(range(leng))
# 	t = timeit.Timer('l[random.randrange(%d)]' % leng,'from __main__ import l, random')
# 	print('list access time: ',t.timeit(number=1000))


#verificar que get e set do dicionário é O(1)
# length = [1000, 10000, 100000, 1000000, 10000000]
# for leng in length:
# 	d = {i:None for i in range(leng)}
# 	t = timeit.Timer('d[random.randrange(%d)]' % leng,'from __main__ import d, random')
# 	print('dict access time: ',t.timeit(number=1000))
# 	t = timeit.Timer('d[random.randrange(%d)] = 1' % leng,'from __main__ import d, random')
# 	print('dict set time: ',t.timeit(number=1000))


# comparar performance do operador del de uma lista com dicionário
# length = [1000000, 10000000] #número muito alto porque como está 
# 							 #deletando aleatoriamente, quanto menor o número, maior probabilidade de tentar acessar indice já deletado
# for leng in length:
# 	l = list(range(leng))
# 	d = {i:None for i in range(leng)}
# 	t = timeit.Timer('del l[random.randrange(%d)]' % leng,'from __main__ import l, random')
# 	print('list del element time: ',t.timeit(number=1000))
# 	t = timeit.Timer('del d[random.randrange(%d)]' % leng,'from __main__ import d, random')
# 	print('dict del element time: ',t.timeit(number=1000))


