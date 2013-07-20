#-*- coding: utf-8 -*-

ano = int(raw_input("Informe o ano em que você nasceu: "))
mes = int(raw_input("Informe o mes em que você nasceu: "))
dia = int(raw_input("Informe o dia em que você nasceu: "))

total_dias = (ano * 365) + (mes * 30) + dia

print "Idade em dias: %d" % total_dias