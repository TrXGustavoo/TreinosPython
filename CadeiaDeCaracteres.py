# Python
# Manipulando string
#         começa em 0
# 	frase = Curso em Video Python
# Fatiamento
# 	frase[9] = V
# 	frase[9:13] = Vide
# 	frase[9:14] = Video
# 	frase[9:21] = Video Python
# 	frase[9:21:2] = Vdo Pto
# 	frase[:5] = Curso
# 	frase[15:] = Python
# 	frase[9::3] = VePh
# Análise
# 	len(frase) = 21
# 	frase.count('o') = 3
# 	frase.count('o',0,13) = 1 porque vai fatiar de 0 ate 12
# 	frase.find('deo') = 11 mostra a posição que começar 
# 	frase.find('Android') = -1 pois nao tem a string Android em frase
# 	'Curso' in frase = true diz se existe Curso em frase
# Trasnformação
# 	frase.replace('Python','Android') = Curso em Video Android substitui Python por Android
# 	frase.upper() = CURSO EM VIDEO PYTHON
# 	frase.lower() = curso em video python
# 	frase.capitalize() = Curso em video python
# 	frase.title() = Curso Em Video Python
# nova frase =   Aprenda Python
# 	frase.strip = Aprenda Python remove os espaços inuteis das pontas
# 	frase.rstrip() = Remove somente os ultimo espaçõs
# 	frase.lstrip() = Remove somento os espaçõs iniciais
# Divisão
# 	frase = Curso em Video Python
# 	frase.split() = Separa as palavras da frase em cadeias de caracteres baseada na quantidade de paçabras
# Junção
# 	'-'.join(frase) = Junta novamente as cadeias de caracteres em unma unica frase com o - Curso-em-Video-Pyhton
