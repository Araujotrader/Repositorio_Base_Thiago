'''Crie um app para calcular a nota média 
de um aluno.
Usuário deve fornecer:
 - Nome do aluno
 - Nota da prova
 - Nota do trabalho
 - Nota de participação
Calcule a média(somar as notas e dividir por 3)

apresente a média do aluno(a)
'''
import time
print('\n_-_-_-_ Calculadora de Média _-_-_-_\n')
aluno = input('Nome do Aluno: ')
prova = float(input('Nota prova: '))
trabalho = float(input('Nota trabalho: '))
part = float(input('Nota participação: '))
nota = (prova + trabalho + part) / 3

print('Calculando...')
time.sleep(1)
print('Calculando.......')
time.sleep(1)
print('Calculando...............')
time.sleep(2)

print(f'''

            Aluno: {aluno}
            Nota: {round(nota,2)}            
 
''')

