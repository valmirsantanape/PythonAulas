"""
pessoa = {'nome': 'valmir', 'sexo': 'M', 'idade': 29}
print(f'O {pessoa["nome"]} é do sexo {pessoa["sexo"]} e tem {pessoa["idade"]} anos')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
del pessoa['sexo']
pessoa['nome'] = 'Leandro'
for k, v in pessoa.items():
    print(f'{k} = {v}')
print()
pessoa['peso'] = 98.5
for k, v in pessoa.items():
    print(f'{k} = {v}')
"""
print()
"""
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2= {'uf': 'São Paulo', 'sigla': 'SP'}
estado3 = {'uf': 'Pernambuco', 'sigla': 'PE'}
estado4 = {'uf': 'Alagoas', 'sigla': 'AL'}
estado5 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
estado6 = {'uf': 'Rio Grande do Sul','sigla': 'RS'}

brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])
"""
print()
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
