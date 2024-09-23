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

    forma_pagamento = input("Escolha a forma de pagamento (avista/cartão): ").strip().lower()

    if forma_pagamento == 'avista':
        desconto = total * 0.10
        total_final = total - desconto
        print(f"Desconto aplicado: R$ {desconto:.2f} (10% à vista)")

    elif forma_pagamento == 'cartão':
        acréscimo = total * 0.10
        total_final = total + acréscimo
        print(f"Acréscimo aplicado: R$ {acréscimo:.2f} (10% no cartão)")

    else:
        print("Forma de pagamento inválida. O total será considerado sem alterações.")
        total_final = total

    os.system("cls || clear")
    print("--- Resumo do Pedido ---")
    print("Pratos escolhidos:")
    for nome, preco in pedidos:
        print(f"{nome} - R$ {preco:.2f}")

    print(f"Subtotal: R$ {total:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Total a pagar: R$ {total_final:.2f}")

menu_principal()
                
                


        

