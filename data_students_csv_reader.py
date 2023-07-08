# Desafio 5: Escreva um programa que leia um arquivo CSV contendo dados de alunos (nome, nota1, nota2) e calcule a média de cada aluno. 
# Em seguida, crie um novo arquivo CSV com o nome do aluno e sua média.

import csv

with open ('data_students.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    next(leitor_csv)

    for linha in leitor_csv:
        print(linha)
    
        nome = linha[0]
        notas = [int(nota) for nota in linha[1:]]
        media = sum(notas) / len(notas)

        print('Aluno', nome)
        print('Média de notas:', media)
        print("")