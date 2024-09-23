import os
os.system("cls || clear")
print(""" 
        CARDÁPIO  
    1 - Strogonoff
    2 - Macarronada
    3 - Feijoada
    4 - Churrasco
    5 - Moqueca de peixe
    6 - Bife à parmegiana
    7 - Lasanha
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

