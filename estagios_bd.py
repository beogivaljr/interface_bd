# Trabalho de PCS 3623 - Banco de dados I
# Alunos:
#   - Beogival Wagner Lucas Santos Junior NUSP: 8992836
#   - Rafael Camargos Santos NUSP: 8041564

import pyrebase

if __name__ == '__main__':

    config = {
        'apiKey': 'AIzaSyAd5C78W8YcEVhWHHtJPVcKb3QMxLnTU-k',
        'authDomain': 'projetobd-b2fd9.firebaseapp.com',
        'databaseURL': 'https://projetobd-b2fd9.firebaseio.com',
        'storageBucket': 'projetobd-b2fd9.appspot.com'
    }

    firebase = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in
    user = auth.sign_in_with_email_and_password('admin.bd@gmail.com', '123456')

    # Get a reference to the database service
    db = firebase.database()

    while True:
        print('\n\n########################')
        print('Bem vindo ao EstagiUSP!\n')
        print('Experimente pesquisar um aluno com um numero usp de 8992836 à 8992935,\n\
copiar seu nome e em seguida usa-lo para fazer um match.')
        print('########################\n\n')
        print('0.Sair   1.Cadastrar   2.Pesquisar   3.Match')
        command = input('Escolha a operação: ')

        if '0' in command:  # Sair
            break
        elif '1' in command:  # Cadastrar
            print('1.Aluno   2.Empresa   3.Currículo   4.Vaga')
            command = input('Escolha a operação: ')
            if '1' in command:  # Aluno
                print('\n##################')
                print('Cadastrando novo aluno!')
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

            elif '2' in command:  # Empresa
                print('\n##################')
                print('Cadastrando nova empresa!')
                nome = input('Digite o nome da empresa: ')
                email = input('Digite o email da empresa: ')
                cnpj = input('Digite o CNPJ da empresa: ')
                telefone = input('Digite o telefone da empresa: ')

                # data to save
                empresa = {
                    'nome': f'{nome}',
                    'email': f'{email}',
                    'telefone': f'{telefone}'
                }

                results = db.child('empresa').child(f'{cnpj}').set(empresa)
                print('Empresa cadastrada com sucesso!')

            elif '3' in command:  # Currículo
                print('\n##################')
                print('Cadastrando novo currículo!')
                nusp = input('Digite o número USP do aluno: ')
                salario = input('Digite a pretensão salarial do aluno: ')
                web = input('Digite o nível de experiência web de 0 a 5: ')
                mobile = input('Digite o nível de experiência mobile de 0 a 5: ')
                back = input('Digite o nível de experiência backend de 0 a 5: ')

                # data to save
                curriculum = {
                    'nusp': f'{nusp}',
                    'pretensão salarial': f'{salario}',
                    'experiencia web': f'{web}',
                    'experiencia mobile': f'{mobile}',
                    'experiencia backend': f'{back}'
                }

                results = db.child('curriculo').push(curriculum)
                print('Currículo cadastrado com sucesso!')

            elif '4' in command:  # Vaga
                print('\n##################')
                print('Cadastrando nova vaga!')
                cnpj = input('Digite o CNPJ da empresa: ')
                salario = input('Digite o valor da bolsa oferecida: ')
                web = input('Digite o requisito de experiência web de 0 a 5: ')
                mobile = input('Digite o requisito de experiência mobile de 0 a 5: ')
                back = input('Digite o requisito de experiência backend de 0 a 5: ')

                # data to save
                vaga = {
                    'cnpj': f'{cnpj}',
                    'requisito web': f'{web}',
                    'requisito mobile': f'{mobile}',
                    'requisito backend': f'{back}',
                    'bolsa': f'{salario}',
                }

                results = db.child('vaga').push(vaga)
                print('Currículo cadastrado com sucesso!')

        elif '2' in command:  # Pesquisar
            print('1.Aluno   2.Empresa   3.Currículo')
            command = input('Escolha a operação: ')
            if '1' in command:  # Aluno
                while True:
                    try:
                        print('Buscar por:')
                        print('0.SAIR   1.Numero USP   2.Nome')
                        command = input('Escolha a operação: ')
                        value = None
                        if '0' in command:  # Sair
                            break
                        elif '1' in command:  # Numero USP
                            nusp = input('Digite o numero USP do aluno (8992836 à 8992935): ')
                            aluno = db.child('aluno').child(nusp).get()
                            value = aluno.val()

                        elif '2' in command:  # Nome
                            input_nome = input('Digite o nome do aluno: ')
                            aluno = db.child('aluno').order_by_child('nome').equal_to(input_nome).get()
                            aluno = aluno.val().items()
                            for key, val in aluno:
                                value = val

                        else:
                            break

                        print('##################')
                        name = '\nNome do aluno: ' + value['nome']
                        curso = '\nCurso: ' + value['curso']
                        periodo = '\nPeríodo do aluno: ' + value['periodo']
                        telefone = '\nTelefone para contato: ' + value['telefone']
                        print(f'{name}{curso}{periodo}{telefone}')

                        break
                    except Exception as e:
                        print(e)

            elif '2' in command:  # Empresa
                while True:
                    try:
                        print('Buscar por:')
                        print('0.SAIR   1.CNPJ   2.Nome')
                        command = input('Escolha a operação: ')
                        value = None
                        if '0' in command:  # Sair
                            break
                        elif '1' in command:  # CNPJ
                            cnpj = input('Digite o CNPJ da empresa: ')
                            empresa = db.child('empresa').child(cnpj).get()
                            value = empresa.val()

                        elif '2' in command:  # Nome
                            input_nome = input('Digite o nome da empresa: ')
                            empresa = db.child('empresa').order_by_child('nome').equal_to(input_nome).get()
                            empresa = empresa.val().items()
                            for key, val in empresa:
                                value = val

                        else:
                            break

                        print('##################')
                        name = value['nome']
                        email = value['email']
                        telefone = value['telefone']
                        company_name = '\nNome da empresa: ' + name
                        mask_key = f'{key[:2]}.{key[2:5]}.{key[5:8]}/{key[8:12]}-{key[12:]}'
                        cnpj = '\nCNPJ: ' + mask_key
                        email_info = '\nE-mail da empresa: ' + email
                        phone_info = '\nTelefone para contato: ' + telefone
                        print(f'{company_name}{cnpj}{email_info}{phone_info}')

                        break
                    except Exception as e:
                        print(e)

            elif '3' in command:  # Currículo
                while True:
                    try:
                        value = None
                        nusp = input('Digite o Numero USP do aluno: ')
                        curriculo = db.child('curriculo').order_by_child('nusp').equal_to(nusp).get()
                        curriculo = curriculo.val().items()
                        for key, val in curriculo:
                            value = val

                        print('##################')
                        nusp = '\nNumero USP do aluno: ' + value['nusp']
                        pay = '\nPretensão salarial: ' + value['pretensão salarial']
                        web = '\nExperiencia web: ' + value['experiencia web']
                        mobile = '\nExperiencia mobile: ' + value['experiencia mobile']
                        back = '\nExperiencia backend: ' + value['experiencia backend']
                        print(f'{nusp}{pay}{web}{mobile}{back}')

                        break
                    except Exception as e:
                        print(e)

        elif '3' in command:  # Match
            while True:
                print('\n##################')
                nome = input('Digite o nome do aluno: ')
                aluno = db.child('aluno').order_by_child('nome').equal_to(nome).get()
                try:
                    for nusp, value in aluno.val().items():
                        curriculo = db.child('curriculo').order_by_child('nusp').equal_to(nusp).get()
                        for key, curriculo in curriculo.val().items():
                            vagas = db.child('vaga').get()
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
                                empresa = db.child('empresa').child(vaga_combinada['cnpj']).get()
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
                            print('\n\n########################')
                            print('Contrato assinado!')
                            print('########################\n\n')
                            break
                    break
                except Exception as e:
                    print(e)
                    print('\n#####################\nAluno não encontrado!\n#####################\n')
