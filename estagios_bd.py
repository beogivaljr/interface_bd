import pyrebase
from faker import Faker
import json
import names
from random import randint

if __name__ == '__main__':

    faker = Faker('pt_BR')

    config = {
        "apiKey": "AIzaSyAd5C78W8YcEVhWHHtJPVcKb3QMxLnTU-k",
        "authDomain": "projetobd-b2fd9.firebaseapp.com",
        "databaseURL": "https://projetobd-b2fd9.firebaseio.com",
        "storageBucket": "projetobd-b2fd9.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in
    user = auth.sign_in_with_email_and_password('admin.bd@gmail.com', '123456')

    # Get a reference to the database service
    db = firebase.database()

    # Alunos
    # nusp = 8992836  # Valor inicial
    #
    # for i in range(100):
    #     courses = ['Engenharia de Computação', 'Engenharia Civil', 'Engenharia Elétrica']
    #     course_index = randint(0, 2)
    #
    #     # data to save
    #     aluno = {
    #         'nome': f'{faker.name()}',
    #         'curso': f'{courses[course_index]}',
    #         'periodo': f'{randint(1, 10)}',
    #         'telefone': f'(11) 9{randint(8000, 9999)}-{randint(1000, 9999)}'
    #     }
    #
    #     results = db.child('aluno').child(f'{nusp}').set(aluno)
    #     nusp += 1
    #     print(results)

    # Empresas
    # for i in range(6):
    #     companies = ['M2Y', 'Outsmart', 'BTG', 'tembici', 'itau', 'livup']
    #
    #     # data to save
    #     companie = {
    #         'nome': f'{companies[i]}',
    #         'email': str(names.get_first_name()) + "@gmail.com",
    #         'telefone': f'(11) {randint(2000, 9999)}-{randint(1000, 9999)}'
    #     }
    #
    #     results = db.child('empresa').child(f'{randint(10000000000000, 99999999999999)}').set(companie)
    #     print(results)

    # Curriculo
    # nusp = 8992836  # Valor inicial
    #
    # for i in range(100):
    #     # data to save
    #     curriculo = {
    #         'nusp': f'{nusp}',
    #         'pretensão salarial': f'{randint(1500, 4000)}',
    #         'experiencia web': f'{randint(0, 5)}',
    #         'experiencia mobile': f'{randint(0, 5)}',
    #         'experiencia backend': f'{randint(0, 5)}'
    #     }
    #
    #     results = db.child('curriculo').push(curriculo)
    #     nusp += 1
    #     print(results)

    # Vagas
    # for i in range(60):
    #     companies = ['19108766731792', '28873925165220', '44113054680588', '58698868711024', '60762866327293', '63730340628396']
    #     # data to save
    #     vaga = {
    #         'cnpj': companies[randint(0, 5)],
    #         'requisito web': f'{randint(0, 5)}',
    #         'requisito mobile': f'{randint(0, 5)}',
    #         'requisito backend': f'{randint(0, 5)}',
    #         'bolsa': f'{randint(1500, 4000)}',
    #     }
    #
    #     results = db.child('vaga').push(vaga)
    #     print(results)

    # Contrato
    # contrato: {
    #     nusp: '',
    #     cnpj: '',
    #     vaga: '',
    #     duração: f'{randint(4, 12)}',
    # }

    while True:
        print('Bem vindo ao EstagiUSP!')
        print('1.Cadastrar   2.Pesquisar   3.Match')
        command = input('Escolha a operação: ')

        if '1' in command:
            print('1.Aluno   2.Empresa   3.Currículo   4.Vaga')
            command = input('Escolha a operação: ')
            if '1' in command:
                nome = input('Digite o nome do aluno: ')
                nusp = input('Digite o número USP do aluno: ')
                curso = input('Digite o curso do aluno: ')
                periodo = input('Digite o período do aluno: ')
                telefone = input('Digite o telefone do aluno: ')

                # data to save
                aluno = {
                    'nome': f'{nome}',
                    'curso': f'{curso}',
                    'periodo': f'{periodo}',
                    'telefone': f'{telefone}'
                }

                results = db.child('aluno').child(f'{nusp}').set(aluno)
                print('Aluno cadastrado com sucesso!')

        elif '2' in command:
            print('1.Aluno   2.Empresa   3.Currículo   4.Vaga')
            command = input('Escolha a operação: ')
            if '2' in command:
                while True:
                    try:
                        print('Buscar por:')
                        print('0.SAIR   1.CNPJ   2.Nome')
                        command = input('Escolha a operação: ')
                        if '0' in command:
                            break
                        elif '2' in command:
                            input_nome = input('Digite o nome da empresa: ')
                            empresa = db.child("empresa").order_by_child("nome").equal_to(input_nome).get()
                            print(empresa.val())
                            break
                    except Exception:
                        pass

        elif '3' in command:
            while True:
                nome = input('Digite o nome do aluno: ')
                aluno = db.child('aluno').order_by_child("nome").equal_to(nome).get()
                try:
                    for nusp, value in aluno.val().items():
                        curriculo = db.child("curriculo").order_by_child("nusp").equal_to(nusp).get()
                        for key, curriculo in curriculo.val().items():
                            vagas = db.child("vaga").get()
                            vagas_combinadas = []
                            keys_vagas_combinadas = []
                            for key_vaga, vaga in vagas.val().items():
                                if vaga['bolsa'] >= curriculo['pretensão salarial'] \
                                        and curriculo['experiencia web'] >= vaga['requisito web']\
                                        and curriculo['experiencia mobile'] >= vaga['requisito mobile']\
                                        and curriculo['experiencia backend'] >= vaga['requisito backend']:
                                    vagas_combinadas.append(vaga)
                                    keys_vagas_combinadas.append(key_vaga)
                            empresas_combinadas = []
                            print('Em qual empresa você gostaria de trabalhar?')
                            i = 0
                            for vaga_combinada in vagas_combinadas:
                                i += 1
                                empresa = db.child("empresa").child(vaga_combinada['cnpj']).get()
                                empresas_combinadas.append(empresa)
                                nome_empresa = empresa.val()['nome']
                                bolsa_empresa = vaga_combinada['bolsa']
                                print(f'{i}. {nome_empresa} com uma bolsa de R${bolsa_empresa},00')
                            i = int(input('Escolha o número: '))
                            contrato = {
                                'nusp': nusp,
                                'cnpj': empresas_combinadas[i-1].key(),
                                'vaga': keys_vagas_combinadas[i-1]
                            }
                            db.child('contrato').push(contrato)
                            print('\n\n############\nParabéns, você está contratado!\n############\n\n')
                    break
                except Exception:
                    print('Aluno não encontrado!')
