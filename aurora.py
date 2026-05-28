#Listas Globais
leituras = []

# Descrição do Projeto
def descricao():
    print("Descricao do projeto")

# Registro de Leituras
def registrar_leitura():
    print("■" * 40)

    energia = validar_float("Energia (0 a 500kWh): ", 0, 500)
    temp = validar_float("Temperatura (-50 a 150°C): ", -50, 150)

    if energia > 200:
        estado = "DIA"
    elif energia >= 48:
        estado = "NOITE"
    else:
        estado = "EMERGENCIA"

    leituras.append({"energia": energia, "temp": temp, "estado": estado})
    print(f"Leitura registrada! Estado: {estado}")
    input("Pressione qualquer tecla para voltar...")
    print("■" * 40)


def validar_float(msg, min, max):
    while True:
        
        num = float(input(msg))
        if min <= num <= max:
            return num
        else:
            print(f"Inválido. Digite um valor entre {min} e {max}.")
    


# Menu Principal
while True:
    print("AURORA - Console da Base XX")
    print("1- Descrição \n2- Registrar \n3- Painel \n4- Autonomia")
    print("5- Relatório \n6- Simular \n0- Sair")

    opcao = input("Opção: ")

    match opcao:
        case "1":
            descricao()
        case "2":
            registrar_leitura()
        case "3":
            print(leituras)
        case "4":
            print("Autonomia")
        case "5":
            print("Relatório")
        case "6":
            print("Simular")
        case "0":
            print("Encerrando AURORA...")
            break
        case _:
            print("Opção inválida")