print("Selecione uma opção:")
print("1. Adição:")
print("2. Subtração:")
print("3. Multiplicação:")
print("4. Divisão:")

opcao = int (input("Escolha uma opção: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if opcao == 1:
    print(f"Resultado: {num1 + num2}")
elif opcao == 2:
    print(f"Resultado: {num1 - num2}")
elif opcao == 2:
    print(f"Resultado: {num1 * num2}")
elif opcao == 2:
    print(f"Resultado: {num1 / num2}")
else:
    print("Opção inválida!")