from cmath import sin
import math
CO = float(input("Comprimento cateto oposto: "))
CA = float(input("Comprimento cateto adjacente: "))
# calcular hipotenusa
HI = math.hypot(CO, CA)
print("A hipotenusa vai medir {:.2f}".format(HI))

