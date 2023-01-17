import pedrapapeltesoura as ppt

while True:
    print('''
            Olá, caro amante das áreas gamer's desse Brasil.
            
            Vamos agora para nosso joguinho. Nos conte:
            
            0 para ENCERRAR O PROGRAMA.
            1 para PEDRA - PAPEL - TESOURA.
    ''')
    tentar = int(input('Digite sua opção: '))
    if tentar == 0: break
    elif tentar == 1: print(ppt.pedrapapeltesoura())