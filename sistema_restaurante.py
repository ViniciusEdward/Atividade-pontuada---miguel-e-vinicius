"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Vinicius Edward da Silva Alves Paixão
2 - Miguel Lemos de Oliveira Esquivel
"""







import os
os.system("cls || clear")
def menu_principal():
    menu = {
        1: ("Strogonoff | R$", 25.00),
        2: ("Macarronada | R$",  15.00),
        3: ("Feijoada | R$", 30.00),
        4: ("Churrasco | R$" , 50.00),
        5: ("Moqueca de peixe | R$" , 30.00),
        6: ("Bife à parmegiana | R$" , 25.00),
        7: ("Lasanha | R$" , 35.00),
    }
    pedidos = []
    total = 0.0

    while True:
        print("Menu de Pratos:")
        for codigo, (nome, preco) in menu.items():
            print(f"{codigo}: {nome} - R$ {preco:.2f}")
        print("0: Finalizar pedido")
        
        codigo = int(input("\nDigite o código do prato desejado: "))
        
        if codigo == 0:
            break

        elif codigo in menu:
            pedidos.append(menu[codigo])
            total += menu[codigo][1]
            print(f"Adicionado: {menu[codigo][0]} - R$ {menu[codigo][1]:.2f}")

        else:
            print("Código inválido. Tente novamente.")
        
        continuar = input("\nDeseja adicionar mais um prato? (s/n): ").strip().lower()
        os.system("cls || clear")
        if continuar != 's':
            break

    if not pedidos:
        print("Nenhum prato foi pedido.")
        return

    os.system("cls || clear")
    print("""=== Formas de pagamento ===
    1 - À vista
    2 - Cartão de crédito  
          """)
    
    forma_pagamento = input("Escolha a forma de pagamento (V) ou (C): ").strip().lower()
    
    os.system("cls || clear")
    print("=== Detalhes do pagamento ===")
    match(forma_pagamento):
        case 'v':
            desconto = total * 0.10
            total_final = total - desconto
            print("Forma de pagamento: À vista")
            print(f"Desconto aplicado: R$ {desconto:.2f} (10% à vista)")
           
        case 'c':
            acréscimo = total * 0.10
            total_final = total + acréscimo
            print("Forma de pagamento: Cartão")
            print(f"Acréscimo aplicado: R$ {acréscimo:.2f} (10% no cartão)")

        case _:
            print("Forma de pagamento inválida. O total será considerado sem alterações.")
            total_final = total

    print("\n=== Resumo do Pedido ===")
    print("Pratos escolhidos:")
    for nome, preco in pedidos:
        print(f"{nome} - R$ {preco:.2f}")

    print(f"Subtotal: R$ {total:.2f}")
    print(f"Total a pagar: R$ {total_final:.2f}")

menu_principal()