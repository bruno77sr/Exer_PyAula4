import math

graus =  int(input("Digite um valor em Graus:"))

rad =  math.radians(graus)

print("O radiano é %.3f " %(rad))
print(" O seno é: %.3f  \nCosseno é: %.3f \nTangente é: %.3f" %(math.sin(rad), math.cos(rad), math.tan(rad)))