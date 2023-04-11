Horas_estimadas = 80
valor_inicial = 1000.00
valor_hora = 20.45
taxa_gordura = 0.15 #15%

valor_total = (valor_inicial + Horas_estimadas * valor_hora) * (1 + taxa_gordura)
valor_total = round(valor_total, 2)

print(f'({valor_total:2f})')
