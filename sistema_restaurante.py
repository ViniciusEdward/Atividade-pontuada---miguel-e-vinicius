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
opcao = int(input("digite a numereção do prato desejado: "))

while True:
    match(opcao):
        case "1":
          print("Strogonoff | R$ 25,00")    
        case "2":
          print("Macarronada | R$ 15,00")    
        case "3":
          print("Feijoada | R$ 30,00")    
        case "4":
          print("Churrasco | R$ 50,00")    
        case "5":
          print("Moqueca de peixe | R$ 30,00")    
        case "1":
          print("Bife à parmegiana | R$ 25,00")    
        case "1":
          print("Lasanha | R$ 35,00")    
        case _:
          print("opção invalida")    

