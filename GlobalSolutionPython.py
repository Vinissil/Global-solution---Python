print("Bem vindo ao seu sistema de registro e monitoramento de saude!")


# Seleciona a ação do usuário
def select_option():
    print("1 - Consultar histórico de dados")
    print("2 - Adicionar nova gravação")
    print("3 - Encerrar o sistema")
    print("")
    option = int(input("Digite a opção desejada: "))
    print("")

    return option


# Verifica qual historico o usuário deseja verificar
def select_history():
    print("O que você deseja consultar?")
    print("1 - Nível de glicose")
    print("2 - Oxigenação no sangue")
    print("3 - Pressão arterial")
    print("")
    entry_option = int(input("Digite a opção desejada: "))
    print("")

    return entry_option


# Verifica qual gravação o usuário deseja adicionar
def append_select():
    print("Qual dado você gostaria de registrar?")
    print("1 - Nível de glicose")
    print("2 - Oxigenação no sangue")
    print("3 - Pressão arterial")
    print("")
    entry_option = int(input("Digite a opção desejada: "))
    print("")

    return entry_option


# Grava os dados fornecidos pelo usuário no array
def add_data(entry):
    # Verifica a data e hora atual
    from datetime import datetime
    new_data = str(input(f"Digite os dados de sua última gravação: "))
    datetime = datetime.now()
    date_format = "%d/%m/%y-%H:%M"
    correct_datetime = datetime.strftime(date_format)
    # Adiciona a data atual e o input do usuário na string
    entry.append(f"{correct_datetime} - {new_data}")
    print(f"{entry_name} adicionado com sucesso!")
    print("")
    print_history(entry)


# Printa o histórco de dados registrados
def print_history(entry):
    print(f"Histórico de {entry_name}:")
    # Percorre o array e printa os dados registrados
    for i in range(len(entry)):
        print(f"{entry[i]}{unit}")
    print("")


# Verifica o input do usuário para determinar as variaveis utilizadas
def conditional():
    if entry_option == 1:
        entry = glicose
        entry_name = "Nível de glicose"
        unit = " mg/dL"

    elif entry_option == 2:
        entry = oxigenacao
        entry_name = "Oxigenação no sangue"
        unit = "%"

    elif entry_option == 3:
        entry = pressao
        entry_name = "Pressão arterial"
        unit = " mmHg"

        return entry, entry_name, unit


# Declara os arrays necessários para gravar e consultar o histórico
glicose = ["28/11/23-01:24 - 85", "30/11/23-07:34 - 87", "01/12/23-01:24 - 83"]
oxigenacao = ["28/11/23-01:24 - 100", "30/11/23-07:34 - 97", "01/12/23-01:24 - 96"]
pressao = ["28/11/23-01:24 - 120/80", "30/11/23-07:34 - 140/90", "01/12/23-01:24 - 110/70"]

print("O que você deseja fazer agora?")
option = select_option()

# Valida o input do usuário
while option < 1 or option > 3:
    print("Opção inválida! Tente novamente")
    option = select_option()

# Loop para o menu de opções
while option != 3:
    if option == 1:
        entry_option = select_history()
        while entry_option < 1 or entry_option > 3:
            print("Opção inválida! Tente novamente")
            entry_option = select_history()

        entry, entry_name, unit = conditional()

        print_history(entry)
        print("O que você deseja fazer agora?")

        option = select_option()

    elif option == 2:
        entry_option = append_select()
        while entry_option < 1 or entry_option > 3:
            print("Opção inválida! Tente novamente")
            entry_option = append_select()

        entry, entry_name, unit = conditional()

        add_data(entry)
        print("O que você deseja fazer agora?")
        option = select_option()

print("Obrigado por utilizar o sistema!")