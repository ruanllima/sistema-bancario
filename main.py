# Valores de ponto de partida
extrato = []
saldo = 0.00
qtd_saque = 0

print("Seja bem-vindo ao Banco Real")
print()

# Inicia um loop até que o usuário o encerre (4).
while True:
    print("""Que operação deseja realizar?
            
            1. Saque
            2. Depósito
            3. Visualizar Extrato
            4. Encerrar""")

    print()
    
    # Inicia um loop que permanece até que o usuário digite um número válido inteiro.
    while True:
        operacao = input("Digite o número correspondente: ")
        print()
        # Converte 'operacao' para inteiro, se der erro imprime uma mensagem e volta para o início.
        try:
            operacao = int(operacao)
            break
        except ValueError:
            print("Número inválido!")

    # Se o número digitado for 1 inicia o loop de saque, e permanece até que o usuário digite um número válido.
    if operacao == 1:
        while True:
            saque = input("Qual o valor que deseja sacar? ")
            try:
                saque = float(saque)
                break
            # Converte 'saque' para float, se der erro imprime uma mensagem e volta para o início.
            except ValueError:
                print("Valor inválido!")
        
        # Se o valor desejado pelo usuário for maior que o saldo, imprime uma mensagem.
        if saque > saldo:
            print()
            print("Infelizmente não será possível realizar esta operação por falta de saldo.")
            print()
        # Se o usuário já tiver feito 3 saques, imprime uma mensagem.
        elif qtd_saque == 3:
            print()
            print("Infelizmente não será possível realizar esta operação devido o limite de 3 saques diários.")
            print()
        # Se o valor desejado pelo usuário for maior que 500, imprime uma mensagem.
        elif saque > 500:
            print()
            print("Infelizmente não será possível realizar esta operação devido o limite de R$ 500,00 por saque.")
            print()
        # Se nenhuma das condições anteriores for atendida, realiza a operação de saque.
        else:
            # Diminui a quantidade sacada de 'saldo'.
            saldo -= saque
            # Cria uma tupla com as informações do saque e adiciona na lista 'extrato'.
            ext = (f"Saque - R$ {saque:.2f}")
            extrato.append(ext)
            # O número de saques aumenta 1.
            qtd_saque += 1
            print()
            print("Saque realizado com sucesso!")
            print()
            
    # Se o número digitado for 2 inicia o loop de depósito, e permanece até que o usuário digite um número válido.
    if operacao == 2:
        while True:
            deposito = input("Digite o valor que deseja depositar: ")
            # Converte 'deposito' para float, se der erro imprime uma mensagem e retorna ao início.
            try:
                deposito = float(deposito)
                break
            except ValueError:
                print("Valor inválido!")
        
        # Adiciona o valor do depósito na variável saldo.
        saldo += deposito
        # Cria uma tupla com as informações do depósito e adiciona na lista 'extrato'.
        ext2 = (f"Depósito - R$ {deposito:.2f}")
        extrato.append(ext2)
        print()
        print("Depósito realizado com sucesso!")
        print()

    # Se o número digitado for 2 inicia o processo de 'visualizar extrato'.
    if operacao == 3:

        # Se a lista extrato estiver vazia, imprime uma mensagem. 
        if extrato == []:
            print("Ainda não há operações realizadas!")

        # Percorre uma lista do tamanho da lista 'extrato' e imprime cada elemento dela pelo índice 'op'.
        for op in range(len(extrato)):
            print(extrato[op])
        
        # Imprime o saldo.
        print()
        print(f"Saldo: R$ {saldo:.2f}")
        print()

    # Se o número digitado pelo usuário for 4, imprime uma mensagem de despedida e encerra o programa.
    if operacao == 4:
        print()
        print("Obrigado por usar nossos serviços!")
        print()
        break
