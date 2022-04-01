#pedindo dados

h = float(input("Digite o valor da altura da pirâmide:"))
Bmaior = float(input("Digite o valor da base maior"))
Bmenor = float(input("Digite o valor da base menor"))

#processamento

volume= h/3*(Bmaior**2+Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

#escrever

print("O volume do tronco é %.2f" %(volume))