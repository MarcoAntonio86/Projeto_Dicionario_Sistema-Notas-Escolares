'''Crie um programa que permita aos professores registrarem notas de alunos e calcular
médias de notas. Use um dicionário onde as chaves são os nomes dos alunos e os
valores são listas de notas.'''

alunos = {}
escolha = 0
c = 0



    
while True:
        quantidade_alunos = input('Quantos alunos deseja cadastrar? ')
        if quantidade_alunos.isdigit():
            quantidade_alunos = int(quantidade_alunos)
            break
        else:
            print('Valor inválido. Por favor, informe um número.')
while True:
        quantidade_notas = input('Quantas notas deseja cadastrar por aluno? ')
        if quantidade_notas.isdigit():
            quantidade_notas = int(quantidade_notas)
            break
        else:
            print('Valor inválido. Por favor, informe um número.')





while c < quantidade_alunos:
    nomes = input('Nome do aluno: ')
    alunos[nomes] = []
    for n in range(0, quantidade_notas):
        while True:
            nota = input(f'Digite a nota {n + 1} do aluno {nomes}: ')
            if nota.replace(".", "", 1).isdigit():  
                alunos[nomes].append(float(nota))
                break
            else:
                print('Valor inválido. Por favor, informe um número.')

    notas_aluno = alunos[nomes]
    media = sum(notas_aluno) / len(notas_aluno)
    print(f'A média do aluno {nomes} é {media:.2f}')

    c += 1

print (f'Alunos: {alunos}')


