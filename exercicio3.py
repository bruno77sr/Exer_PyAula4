ano =  int(input("Que ano você nasceu ?"))
mes =  int(input("Que mês você nasceu ?"))
dia =  int(input("Que dia você nasceu ?"))

idade = 2022 - ano
idadeDias =  360 * idade + (mes * 30)

print("A sua idade em dias é:", idadeDias)