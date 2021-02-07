teste = list()
teste.append('Valmir')
teste.append(29)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('=-' * 20)

galera = [['joao', 19], ['Ana', 23], ['Joaquim', 40], ['Maria', 26]]
print(galera[0])
print(galera[0][0])
print(galera[0][1])
print(galera[1][0])
print(galera[1][1])
print()
print('=-' * 20)
print()
for p in galera:
    print(p[0])

print('=-' * 20)
