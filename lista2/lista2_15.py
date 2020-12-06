numeroinicial = (int(input("Digite o numero inicial: ")))
numerofinal = (int(input("Digite o numero final: ")))

contadorperfeitos = 0
auxIntervalo = numeroinicial

for i in range(numeroinicial, numerofinal):
  somatorioPerfeito = 0
  for j in range(1, i-1):
    if (i % j == 0):
      somatorioPerfeito += j

  if (somatorioPerfeito == i):
    contadorperfeitos += 1
    print("Numero perfeito: ", i)

print("A quantidade de perfeitos é: ", contadorperfeitos)
