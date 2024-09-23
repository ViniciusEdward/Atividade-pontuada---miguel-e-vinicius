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
          print("\nstrogonoff | R$ 25,00")    
        case "2":
          print("\nMacarronada | R$ 15,00")    
        case "3":
          print("\nfeijoada | R$ 30,00")    
        case "4":
          print("\nchurrasco | R$ 50,00")    
        case "5":
          print("\nmoqueca de peixe | R$ 25,00")    
        case "1":
          print("\nstrogonoff | R$ 25,00")    
        case "1":
          print("\nstrogonoff | R$ 25,00")    
        case "1":
          print("\nstrogonoff | R$ 25,00")    

