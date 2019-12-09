from faker import Faker
import json
import names
from random import randint

# Alunos
#     nusp = 8992836  # Valor inicial
#
#     for i in range(100):
#         courses = ['Engenharia de Computação', 'Engenharia Civil', 'Engenharia Elétrica']
#         course_index = randint(0, 2)
#
#         # data to save
#         aluno = {
#             'nome': f'{faker.name()}',
#             'curso': f'{courses[course_index]}',
#             'periodo': f'{randint(1, 10)}',
#             'telefone': f'(11) 9{randint(8000, 9999)}-{randint(1000, 9999)}'
#         }
#
#         results = db.child('aluno').child(f'{nusp}').set(aluno)
#         nusp += 1
#         print(results)
#
#     Empresas
#     for i in range(6):
#         companies = ['M2Y', 'Outsmart', 'BTG', 'tembici', 'itau', 'livup']
#
#         # data to save
#         companie = {
#             'nome': f'{companies[i]}',
#             'email': str(names.get_first_name()) + '@gmail.com',
#             'telefone': f'(11) {randint(2000, 9999)}-{randint(1000, 9999)}'
#         }
#
#         results = db.child('empresa').child(f'{randint(10000000000000, 99999999999999)}').set(companie)
#         print(results)
#
#     Curriculo
#     nusp = 8992836  # Valor inicial
#
#     for i in range(100):
#         # data to save
#         curriculo = {
#             'nusp': f'{nusp}',
#             'pretensão salarial': f'{randint(1500, 4000)}',
#             'experiencia web': f'{randint(0, 5)}',
#             'experiencia mobile': f'{randint(0, 5)}',
#             'experiencia backend': f'{randint(0, 5)}'
#         }
#
#         results = db.child('curriculo').push(curriculo)
#         nusp += 1
#         print(results)
#
#     Vagas
#     for i in range(60):
#         companies = ['19108766731792',\
#         '28873925165220',\
#         '44113054680588',\
#         '58698868711024',\
#         '60762866327293',\
#         '63730340628396']
#         # data to save
#         vaga = {
#             'cnpj': companies[randint(0, 5)],
#             'requisito web': f'{randint(0, 5)}',
#             'requisito mobile': f'{randint(0, 5)}',
#             'requisito backend': f'{randint(0, 5)}',
#             'bolsa': f'{randint(1500, 4000)}',
#         }
#
#         results = db.child('vaga').push(vaga)
#         print(results)
#
#     Contrato
#     contrato: {
#         nusp: '',
#         cnpj: '',
#         vaga: '',
#         duração: f'{randint(4, 12)}',
#     }
