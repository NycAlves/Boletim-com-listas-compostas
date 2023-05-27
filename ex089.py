boletim = dict()
boletim['Nome'] = str(input('Nome do aluno: '))
boletim['Media'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Media'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Media'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
print('--'*30)
for k, v in boletim.items():
    print(f'-{k} é igual a {v}')
