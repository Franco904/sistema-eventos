class TelaParticipante:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print('-------- PARTICIPANTES ----------')
        print('1 - Adicionar participante')
        print('2 - Excluir participante')
        print('3 - Alterar participante')
        print('4 - Consultar participante')
        print('5 - Listar participantes')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pegar_dados_participante(self):
        print('-------- CADASTRAR PARTICIPANTE ----------')
        cpf = input('CPF: ')
        nome = input('Nome: ')
        ano = input('Ano de nascimento: ')
        mes = input('Mês de nascimento: ')
        dia = input('Dia de nascimento: ')
        logradouro = input('Logradouro (endereço): ')
        num_endereco = input('Número (endereço): ')
        cep = input('CEP (endereço): ')

        return {'cpf': cpf, 'nome': nome, 'ano': ano, 'mes': mes, 'dia': dia,
                'logradouro': logradouro, 'num_endereco': num_endereco, 'cep': cep}

    def consultar_participante(self, dados_participante):
        print('CPF DO PARTICIPANTE: ', dados_participante['cpf'])
        print('NOME DO PARTICIPANTE: ', dados_participante['nome'])
        print('DATA DE NASCIMENTO DO PARTICIPANTE: ', dados_participante['data_nascimento'])
        print('ENDEREÇO DO PARTICIPANTE: ', dados_participante['endereco'])
        print('\n')

    def selecionar_participante(self):
        cpf = input('CPF do participante que deseja selecionar: ')
        return cpf

    def mostrar_mensagem(self, msg):
        print(msg)
