while True:
    i = 0
    x = int(input("Digite um número para ver sua tabuada: "))
    if x < 0:
        break
    for c in range(1, 11, 1):
        if c < 10:
            i = x * c
            if i < 10:
                print("{} X 0{} = 0{}".format(x, c, x*c))
            else:
                print("{} X 0{} = {:2}".format(x, c, x*c))
    print("{} X {} = {}".format(x, c, x*c))
print('Programa de tabuada encerrado')
