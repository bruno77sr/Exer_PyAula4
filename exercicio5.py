import math

graus =  int(input("Digite um valor em Graus:"))

rad =  graus / 180

print(" O seno é: %.2f  \nCosseno é: %.2f \nTangente é: %.2f" %(math.sin(rad), math.cos(rad), math.tan(rad)))