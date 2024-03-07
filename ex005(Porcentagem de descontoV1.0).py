p = float(input("Qual o preço do produto? R$"))
d = int(input("Porcentagem de desconto: "))
np = p - (p * (d/100)) 
print("O produto que custava R${} na promoção com desconto de {}%  vai custar R${:.2f}".format(p, d, np))