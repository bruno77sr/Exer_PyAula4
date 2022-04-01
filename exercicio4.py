valorPrestacao = float(input("Digite o valor da prestação:"))
multa  = float(input("Digite a porcentagem de multa"))
qtdDias = int (input("Quantos dias está atrasado"))

prestacao =  valorPrestacao + valorPrestacao* (multa/100)*qtdDias

print("O valor da prestação é %.3f" %(prestacao))