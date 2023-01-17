import time as tm
import os
import random

# O jogo.
def pedrapapeltesoura():
    # lista para possibilidades do jogo.
    possivel = ["pedra", "papel", "tesoura"]
    while True:
        print('''
            Olá, caro gamer! Seja muito bem vindo(a) ao jogo Pedra-Papel-Tesoura.   
    ''')
        tm.sleep(2)
        try:
            os.system('cls')
        except:
            os.system('clear')
        
        print('''
            Para começarmos, preciso saber:
            0 - multiplayer (2 jogadores humanos).
            1 - singleplayer (1 jogador humano contra mim - máquina -)
    ''')

        single_multi = int(input('Digite 0 para multi player e 1 para single player: '))

        tm.sleep(2)
        try:
            os.system('cls')
        except:
            os.system('clear')
        while single_multi == 0:
            print('''
            Olá, caro gamer! O primeiro player deve escolher entre pedra, papel e tesoura. Vou ler e ocultar a resposta e, em seguida, o segundo player irá fazer sua escolha.
            Após alguns segundos apresentarei o resultado. Sendo que:
            digite 0 para PEDRA
            digite 1 para PAPEL
            digite 2 para TESOURA
            P1    -  P2   => RESULTADO
            PEDRA - PEDRA => EMPATE
            PAPEL - PAPEL => EMPATE
            TESOURA - TESOURA => EMPATE
            PEDRA - PAPEL => P2 VENCE
            PEDRA - TESOURA => P1 VENCE
            PAPEL - PEDRA => P1 VENCE
            PAPEL - TESOURA => P2 VENCE
            TESOURA - PEDRA => P2 VENCE
            TESOURA - PAPEL => P1 VENCE
        ''')
        
            p1 = int(input('Digite a opção do P1: '))
            try:
                os.system('cls')
            except:
                os.system('clear')
            p2 = int(input('Digite a opção do P2: '))
            try:
                os.system('cls')
            except:
                os.system('clear')
            
            jogadaP1 = possivel[p1]
            jogadaP2 = possivel[p2]
        
            if jogadaP1 == jogadaP2:
                print(f'''
                Olá, caro gamers! O resultado foi:
                P1 - P2 => RESULTADO
                {jogadaP1} - {jogadaP2} => EMPATE     
            ''')
            elif (jogadaP1 == "pedra" and jogadaP2 == "tesoura") or (jogadaP1 == "papel" and jogadaP2 == "pedra") or (jogadaP1 == "tesoura" and jogadaP2 == "papel"):
                print(f'''
                Olá, caro gamers! O resultado foi:
                P1 - P2 => RESULTADO
                {jogadaP1} - {jogadaP2} => P1 VENCEU    
            ''')
            else:
                print(f'''
                Olá, caro gamers! O resultado foi:
                P1 - P2 => RESULTADO
                {jogadaP1} - {jogadaP2} => P2 VENCEU   
            ''')
            print('''
                Olá, caro gamer! Deseja jogar novamente? S para SIM e N para NÃO
        ''')
            if input() == "N": break
            tm.sleep(2)
            try:
                os.system('cls')
            except:
                os.system('clear')
        while single_multi == 1:
            print('''
            Olá, caro gamer! O primeiro player deve escolher entre pedra, papel e tesoura. Vou ler e ocultar a resposta e, em seguida, 'PENSAREI' em uma opção.
            Após alguns segundos apresentarei o resultado. Sendo que:
            digite 0 para PEDRA
            digite 1 para PAPEL
            digite 2 para TESOURA
            P1    -  P2   => RESULTADO
            PEDRA - PEDRA => EMPATE
            PAPEL - PAPEL => EMPATE
            TESOURA - TESOURA => EMPATE
            PEDRA - PAPEL => P2 VENCE
            PEDRA - TESOURA => P1 VENCE
            PAPEL - PEDRA => P1 VENCE
            PAPEL - TESOURA => P2 VENCE
            TESOURA - PEDRA => P2 VENCE
            TESOURA - PAPEL => P1 VENCE
        ''')
        
            p1 = int(input('Digite a opção do P1: '))
            try:
                os.system('cls')
            except:
                os.system('clear')
            p2 = random.choice(possivel)
            try:
                os.system('cls')
            except:
                os.system('clear')
            
            jogadaP1 = possivel[p1]
            jogadaP2 = p2
        
            if jogadaP1 == jogadaP2:
                print(f'''
                Olá, caro gamers! O resultado foi:
                P1 - COMPUTADOR => RESULTADO
                {jogadaP1} - {jogadaP2} => EMPATE     
            ''')
            elif (jogadaP1 == "pedra" and jogadaP2 == "tesoura") or (jogadaP1 == "papel" and jogadaP2 == "pedra") or (jogadaP1 == "tesoura" and jogadaP2 == "papel"):
                print(f'''
                Olá, caro gamers! O resultado foi:
                P1 - COMPUTADOR => RESULTADO
                {jogadaP1} - {jogadaP2} => P1 VENCEU    
            ''')
            else:
                print(f'''
                Olá, caro gamers! O resultado foi:
                P1 - COMPUTADOR => RESULTADO
                {jogadaP1} - {jogadaP2} => COMPUTADOR VENCEU   
            ''')
            print('''
                Olá, caro gamer! Deseja jogar novamente? S para SIM e N para NÃO
        ''')
            if input() == "N": break
            tm.sleep(2)
            try:
                os.system('cls')
            except:
                os.system('clear')
        print('''
            Olá, caro gamer! Deseja recomeçar? S para SIM e N para NÃO
    ''')
        if input() == "N": break