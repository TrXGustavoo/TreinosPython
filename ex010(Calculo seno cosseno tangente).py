from cmath import cos, sin
import math
ang = float(input("Digite o ângulo que você deseja: "))
# pegar o input da var angulo transformar em radiano e calcula o seno 
Sen = math.sin(math.radians(ang))
Cos = math.cos(math.radians(ang))
Tg = math.tan(math.radians(ang))
print("O angulo {:.2f} tem o seno de {:.2f} o cosseno de {:.2f} e a tangente de {:.2f}".format(ang, Sen, Cos, Tg))
