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
        print('\n\n########################\nBem vindo ao EstagiUSP!\n########################\n\n')
        print('1.Cadastrar   2.Pesquisar   3.Match')
        command = input('Escolha a operação: ')

        if '1' in command:
            print('1.Aluno   2.Empresa   3.Currículo   4.Vaga')
            command = input('Escolha a operação: ')
            if '1' in command:
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
                    'período': f'{periodo}',
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
                            empresa = db.child('empresa').order_by_child('nome').equal_to(input_nome).get()

                            for key, value in empresa.val().items():
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

        elif '3' in command:
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
                            print('\n\n########################\n\
                            Parabéns, você está contratado!\n########################\n\n')
                    break
                except Exception as e:
                    print(e)
                    print('\n#####################\nAluno não encontrado!\n#####################\n')
