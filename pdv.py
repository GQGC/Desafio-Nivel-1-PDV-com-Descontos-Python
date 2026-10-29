historico = []

print("=== Sistema de Caixa / Compras ===")
print("Digite 0 no valor da compra para encerrar e ver o resumo.")

while True:
    valor_original = float(input("\nDigite o valor da compra em reais: "))

    # Condição de saída do loop
    if valor_original == 0:
        break
        
    idade = int(input("Digite a idade do cliente: "))
    
    # Validação simples para valores negativos
    if valor_original < 0 or idade < 0:
        print("Aviso: O valor da compra e a idade não podem ser negativos. Tente novamente.")
        continue
        
    # Regra 1: Desconto por idade (20% se idade >= 65)
    if idade >= 65:
        valor_intermediario = valor_original * 0.8
    else:
        valor_intermediario = valor_original
        
    # Regra 2: Desconto por valor (10% extra se o valor intermediário for > 100)
    if valor_intermediario > 100:
        valor_final = valor_intermediario * 0.9
    else:
        valor_final = valor_intermediario
        
    desconto_aplicado = valor_original - valor_final
    
    # Guardando a compra no histórico
    historico.append((valor_original, valor_final, desconto_aplicado))
    
    # Exibindo o valor final formatado
    print(f"Valor final: R$ {valor_final:.2f}")

# Resumo final após o encerramento do loop
print("\n" + "="*30)
print("=== RESUMO FINAL DO DIA ===")
print("="*30)

quantidade_compras = len(historico)

if quantidade_compras > 0:
    total_bruto = sum(item[0] for item in historico)
    total_descontos = sum(item[2] for item in historico)
    total_final = sum(item[1] for item in historico)
    
    print(f"Quantidade de compras registradas: {quantidade_compras}")
    print(f"Total bruto: R$ {total_bruto:.2f}")
    print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
    print(f"Total final: R$ {total_final:.2f}")
else:
    print("Nenhuma compra foi registrada.")
print("="*30)