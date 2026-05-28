# Bibliotecas
import math

# Listas Globais
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
    input("> Pressione qualquer tecla para voltar...")
    print("■" * 40)

## Validação de entradas numéricas
def validar_float(msg, min, max):
    while True:
        
        num = float(input(msg))
        if min <= num <= max:
            return num
        else:
            print(f"Inválido. Digite um valor entre {min} e {max}.")
    

#Painel de Status
def painel_status():
    print("■" * 40)
    if len(leituras) == 0:
        print("Nenhuma leitura registrada.")
        print("Diriga-se a opção 2 para registrar leituras.")
    else:
        ultimaLeitura = leituras[-1]
        print(f"Estado: {ultimaLeitura["estado"]}")
        print(f"Energia: {ultimaLeitura["energia"]}kWh")
        print(f"Temperatura: {ultimaLeitura["temp"]}°C")
        print(f"Total de leituras: {len(leituras)}")
    input("> Pressione qualquer tecla para voltar...")
    print("■" * 40)

# Cálculo de Autonomia
def calcular_autonomia(e0, k = 0.067, eseg = 48):
    if e0 <= eseg:
        return 0
    return (1/k) * math.log(e0/eseg)

## Submenu de Autonomia

def opcao_autonomia():
    print("■" * 40)
    e0 = validar_float("Reserva atual (0 a 500kWh): ", 0, 500)
    taxa = validar_float("Taxa de consumo (0 a 50kWh): ", 0, 50)
    horas = calcular_autonomia(e0, k = taxa/e0 if (e0 > 0) and (taxa > 0) else 0.067)
    
    print(f"Autonomia estimada: {horas:.1f} horas")
    print(f"Noite lunar dura: ~336 horas")

    if horas < 336:
        print("ATENÇÃO: Reserva insuficiente para a noite inteira!")

    input("> Pressione qualquer tecla para voltar...")
    print("■" * 40)

# Relatório de Consumo
def relatorio_consumo():
    print("■" * 40)
    if len(leituras) == 0:
        print("Nenhuma leitura registrada.")
        print("Diriga-se a opção 2 para registrar leituras.")
    else:
        leituras_energia = []

        for leitura in leituras:
            leituras_energia.append(leitura["energia"])

        total = sum(leituras_energia)
        media = total / len(leituras_energia)
        maximo = max(leituras_energia)
        minimo = min(leituras_energia)

        print(f"Número de Leituras: {len(leituras_energia)}")
        print(f"Energia Total: {total:.1f}kWh")
        print(f"Energia Média: {media:.1f}kWh")
        print(f"Energia Máxima: {maximo:.1f}kWh")
        print(f"Energia Mínima: {minimo:.1f}kWh")

    input("> Pressione qualquer tecla para voltar...")
    print("■" * 40)
    
# Simulação de Cenário
def simular_cenario():
    print("■" * 40)
    print("Escolha o cenário: ")
    print("1- Noite Normal (e0 = 120, k = 0.067)")
    print("2- Noite Prolongada (e0 = 80, k = 0.090)")
    print("3- Falha de Painel (e0 = 50, k = 0.067)")
    opcao = input("> Cenário: ")

    match opcao:
        case "1":
            e0 = 120
            k = 0.067
            nome = "Noite Normal"
        case "2":
            e0 = 80
            k = 0.090
            nome = "Noite Prolongada"
        case "3":
            e0 = 50
            k = 0.067
            nome = "Falha de Painel"
        case _:
            print("Opção Inválida")
            input("> Pressione qualquer tecla para voltar...")
            print("■" * 40)
            return
    
    horas = calcular_autonomia(e0, k)
    print(f"Cenário: {nome}")
    print(f"Reserva: {e0}kWh")
    print(f"Autonomia: {horas:.1f} horas")
    
    input("> Pressione qualquer tecla para voltar...")
    print("■" * 40)    


# Menu Principal
while True:
    print("AURORA - Console da Base XX")
    print("1- Descrição da Solução\n2- Registrar Leitura\n3- Painel de Status")
    print("4- Calcular Autonomia\n5- Relatório de Consumo\n6- Simular Cenário")
    print("0- Sair")

    opcao = input("> Opção: ")

    match opcao:
        case "1":
            descricao()
        case "2":
            registrar_leitura()
        case "3":
            painel_status()
        case "4":
            opcao_autonomia()
        case "5":
            relatorio_consumo()
        case "6":
            simular_cenario()
        case "0":
            print("Encerrando AURORA...")
            break
        case _:
            print("Opção inválida")