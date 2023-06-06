import re

#funções de validação
#VALIDAÇÃO DO CPF
def validar_cpf(cpf):
    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se o CPF contém apenas dígitos
    if not cpf.isdigit():
        return False

    # Verifica se todos os dígitos do CPF são iguais
    if len(set(cpf)) == 1:
        return False

    # Verifica se o CPF é válido utilizando a fórmula de validação
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    if digito1 != int(cpf[9]):
        return False

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if digito2 != int(cpf[10]):
        return False

    return True


#VALIDAÇÃO DO CEP
def validar_cep(cep):
    # Verifica se o CEP possui 8 dígitos
    if len(cep) != 8:
        return False
    
    # Verifica se o CEP contém apenas dígitos
    if not cep.isdigit():
        return False
    
    return True


#VALIDAÇÃO DO TELEFONE
def validar_telefone(telefone):
    # Remove caracteres não numéricos do telefone
    telefone = re.sub(r'\D', '', telefone)

    # Verifica se o telefone possui 10 ou 11 dígitos
    if len(telefone) != 10 and len(telefone) != 11:
        return False

    # Verifica se o telefone começa com 9 (para números celulares)
    if len(telefone) == 11 and telefone[2] != '9':
        return False

    return True


print("Olá! Seja bem-vindo à plataforma de cadastro da Sabor Solidário.")
resposta = input("Gostaria de realizar o cadastro? (s/n): ")

if resposta.lower() == "n":
    print("Ok! Programa encerrado.")
else:
    print("Ok! Por favor, digite seu nome completo:")
    nome_completo = input()
    print("Agora, digite seu CPF:")
    cpf = input()

    while not validar_cpf(cpf):
        print("CPF inválido. Digite novamente.")
        cpf = input()

    print("Agora, por favor, digite o seu CEP sem traços.")
    cep = input()

    while not validar_cep(cep):
        print("CEP inválido. Digite novamente.")
        cep = input()

    print("Estamos quase acabando! Digite o seu telefone:")
    telefone = input()

    while not validar_telefone(telefone):
        print("Telefone inválido. Digite novamente.")
        telefone = input()

    print(f"{nome_completo}, crie uma senha para você.")
    senha =  input()

    print("Por último, quantas pessoas moram junto à você?")
    qntd_pessoas = input()

    print(f"Certo. Concluímos o seu cadastro, {nome_completo}! \nVocê deseja fazer o login para solicitar nossa marmita solidária? (s/n)" )
    resposta_login = input()

    if resposta_login == "n":
        print("Ok! Quando precisar, volte para realizar o seu login!")
    else:
        print("Ok! Digite o seu nome cadastrado anteriormente, por favor.")
        login_nome = input()
        
        while login_nome != nome_completo:
            print("Nome inválido. Digite novamente.")
            login_nome = input()

        print("Bem-vindo de volta! Faça login com sua senha:")
        login_senha = input()

        while login_senha != senha:
            print("Senha inválida. Digite novamente.")
            login_senha = input()

        while True:
            print("Login realizado com sucesso!")
            print(f"{nome_completo}, o que você deseja fazer em nossa plataforma?")
            print("(1) Solicitar marmita solidária")
            print("(2) Solicitar cesta básica")
            print("(3) Alterar CEP")
            print("(4) Sair")
    
            escolha = input()
            
            if escolha == "1":
                print("Certo! Quantas marmitas solidárias você irá precisar?")
                qntd_marmitas = int(input())
                print("Qual seria o endereço para a entrega?")
                endereco = input()
                print(f"Ok, {nome_completo}! Enviaremos um total de {qntd_marmitas} marmitas para você no seguinte endereço: {endereco}, de CEP: {cep}.")
                print("É necessário mostrar o comprovante de renda bruta no local de entrega.")
                print("OBS: A distribuição de marmitas é somente autorizada se o beneficiário tiver uma renda bruta mensal de até 1 salário mínimo.")
                
            elif escolha == "2":
                print("Ok! Quantas cestas básicas você deseja solicitar?")
                qntd_cestas = int(input())
                print("Qual seria o endereço para a entrega?")
                endereco2 = input()
                print(f"Ok, {nome_completo}! Enviaremos um total de {qntd_cestas} cestas básicas para você no seguinte endereço: {endereco2}, de CEP: {cep}.")
                print("É necessário mostrar o comprovante de renda bruta no local de entrega.")
                print("OBS: A distribuição de cestas básicas é somente autorizada se o beneficiário tiver uma renda bruta mensal de até 1 salário mínimo.")
                
            elif escolha == "3":
                print("Qual será o seu novo CEP?")
                cep_alterado = input()
                print("CEP alterado com sucesso.")
                
            elif escolha == "4":
                print(f"Saindo da plataforma...\nAté mais, {nome_completo}!")
                break
            
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            
            # Adicione uma pausa para exibir o menu novamente
            input("Pressione Enter para continuar...")

        

