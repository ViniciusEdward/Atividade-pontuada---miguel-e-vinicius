import os
os.system("cls || clear")
print(""" 
        CARDÁPIO  
    1 - Strogonoff | R$ 25,00
    2 - Macarronada | R$ 15,00
    3 - Feijoada | R$ 30,00
    4 - Churrasco | R$ 50,00
    5 - Moqueca de peixe | R$ 30,00
    6 - Bife à parmegiana | R$ 25,00
    7 - Lasanha | R$ 35,00
    """)
soma_dos_pedidos = 0

opcao = input("Digite a numereção do prato desejado: ")

match(opcao):
    case "1":
        print("Strogonoff | R$ 25,00")  
        preco_strogonoff = 25  
    case "2":
        print("Macarronada | R$ 15,00")
        preco_macarronada = 15    
    case "3":
        print("Feijoada | R$ 30,00")
        preco_feijoda = 30    
    case "4":
        print("Churrasco | R$ 50,00")    
        preco_churrasco = 50
    case "5":
        print("Moqueca de peixe | R$ 30,00")  
        preco_moqueca = 30  
    case "6":
        print("Bife à parmegiana | R$ 25,00")  
        preco_bife = 25  
    case "7":
        print("Lasanha | R$ 35,00")    
        preco_lasanha = 35
    case _:
        print("opção invalida")    

while True:
    adicionar = input("Deseja adicionar outro prato: A (adicionar) ou 0 (para calcular o valor)")
    
    match(adicionar):
        case 'A':
            opcao = int(input("Digite a numereção do prato desejado: "))
        case "0":
            soma_dos_pedidos += opcao
            pagamento = input("Digite a forma de pagamento: ")
            


    

