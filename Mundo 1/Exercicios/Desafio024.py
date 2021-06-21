"""
ENUNCIADO DO EXERCICIO

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
"""

c = str(input('Digite o nome de uma cidade: ')).strip()
cc = c.lower()
cc = cc.split()
print('santo' in cc[0])
