def main():
    # Menu de pratos
    menu = {
        1: ("Prato 1", 20.00),
        2: ("Prato 2", 25.00),
        3: ("Prato 3", 30.00),
        4: ("Prato 4", 15.00),
        5: ("Prato 5", 18.00),
        6: ("Prato 6", 22.00),
        7: ("Prato 7", 27.00),
    }
    
    # Variáveis para armazenar o pedido
    pedidos = []
    total = 0.0

    while True:
        # Exibir o menu
        print("Menu de Pratos:")
        for codigo, (nome, preco) in menu.items():
            print(f"{codigo}: {nome} - R$ {preco:.2f}")
        print("0: Finalizar pedido")
        
        # Entrada do usuário
        codigo = int(input("Digite o código do prato desejado: "))
        
        if codigo == 0:
            break
        elif codigo in menu:
            pedidos.append(menu[codigo])
            total += menu[codigo][1]
            print(f"Adicionado: {menu[codigo][0]} - R$ {menu[codigo][1]:.2f}")
        else:
            print("Código inválido. Tente novamente.")
        
        # Perguntar se deseja continuar
        continuar = input("Deseja adicionar mais um prato? (s/n): ").strip().lower()
        if continuar != 's':
            break

    # Se não houver pedidos, encerra o programa
    if not pedidos:
        print("Nenhum prato foi pedido.")
        return
    
    # Solicitar forma de pagamento
    forma_pagamento = input("Escolha a forma de pagamento (avista/cartão): ").strip().lower()
    
    # Cálculo do valor final
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
    
    # Resultados finais
    print("\n--- Resumo do Pedido ---")
    print("Pratos escolhidos:")
    for nome, preco in pedidos:
        print(f"{nome} - R$ {preco:.2f}")
    
    print(f"Subtotal: R$ {total:.2f}")
    print(f"Forma de pagamento: {forma_pagamento}")
    print(f"Total a pagar: R$ {total_final:.2f}")
main()