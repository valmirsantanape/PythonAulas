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
