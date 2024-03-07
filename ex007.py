d = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km foram rodados? "))
total = 60 * d + 0.15 * km
print("O total a pagar sera de R${:.2f}".format(total))