import time
from random import randint

jogadores = {}  # Uma dicionário(mapa) que associa um jogador com a quantidade de cérebros consumidos
indexJogadores = []  # Uma lista que recebe as chaves(nomes) do dicionário de jogadores, permitindo acessar os
# jogadores por index
tubo = []  # Uma lista que armazenará dados a serem jogados
indexTubo = 0  # O indíce de qual dado será pego do tubo da próxima vez

# definindo os dados em listas
# o primeiro elemento indica a cor e os demais cada lado do dado
c = 'cérebro'
p = 'passos'
e = 'tiros'
dadoVerde = ['verde', c, c, c, p, p, e]
dadoAmarelo = ['amarelo', c, c, p, p, e, e]
dadoVermelho = ['vermelho', c, p, p, e, e, e]


def iniciar():
    mostraLinha()
    print("\033[1;30;42mBem vindo ao Zombie dice!\033[m")
    mostraLinha()
    time.sleep(0.5)

    selecionarQuantidadeJogadores()

    global indexJogadores
    indexJogadores = list(jogadores)
    mostraLinha()
    print("Vamos começar o banquete de cérebros,\n")
    mostraLinha()
    # Exibe o nome de todos o jogadores
    for count in range(0, len(indexJogadores)):
        print(f'Zumbi {indexJogadores[count]}'.upper())
    time.sleep(0.5)
    while True:
        mostraLinha()
        print("""
      1.Começar o jogo
      2.Mudar os jogadores
      3.Sair
      """)
        mostraLinha()
        escolha = input("Digite: ")

        if escolha == "1":
            time.sleep(0.5)

            time.sleep(0.5)
            mostraLinha()
            print("Vamos jogar!")
            mostraLinha()
            jogoStart()

        # Permite alterar todos os jogadores sem reiniciar o programa
        elif escolha == "2":
            time.sleep(0.5)
            mostraLinha()
            selecionarQuantidadeJogadores()
            mostraLinha()

        # com o elif da escolha sair,o programa é encerrado.
        elif escolha == "3":
            time.sleep(0.5)

            print("\n CÉÉÉREBROS!! ")
            break
        else:

            print("\n Não é uma escolha válida!")


def selecionarQuantidadeJogadores():
    qtd_jogadores = 0

    while qtd_jogadores < 2:
        mostraLinha()
        try:
            qtd_jogadores = int(input("\nInforme o número de jogadores:\n"))
            if qtd_jogadores < 2:
                print('\nQuantidade inválida, o número mínimo de jogadores é 2!')
        except ValueError:
            print("Entrada inválida. Informe um número inteiro!")
        mostraLinha()

    # o uso do for e do nomeJogador.append serve para evitar o trabalho adicional que seria criar uma variável para
    # cada jogador adicionado
    mostraLinha()
    for posicao in range(0, qtd_jogadores):
        # no dict a chave é o nome do jogador, o 0 significa quantidade de pontos do jogador
        jogadores[input(f"Digite o nome do jogador {posicao+1}:\n")] = 0
    mostraLinha()

def resetarJogadores():  # redefine os pontos de todos os jogadores para zero
    for jogador in indexJogadores:
        jogadores[jogador] = 0


def jogoStart():
    rodada_atual = 0

    # Cada iteração do loop while corresponde à uma rodada
    while True:
        rodada_atual += 1
        mostraLinha()
        print("INÍCIO DA RODADA", rodada_atual)
        time.sleep(2)
        mostraLinha()
        for jogador in range(0, len(indexJogadores)):
            # se a jogada retornar true, significa que algum jogador venceu
            if jogada(jogador):
                mostraLinha()
                print(f"O jogador {indexJogadores[jogador]} foi o vencedor!")
                mostraLinha()
                resetarJogadores()
                return jogador  # retorna o vencedor


def inserirDadosNoTubo():
    print("Colocando dados no tubo")
    time.sleep(2)
    qtd_dado_verde = 6
    qtd_dado_amarelo = 4
    qtd_dado_vermelho = 3

    # Coloca os dados no tubo de forma aleatoria
    # TODO: implementar um código eficiente
    while (qtd_dado_verde + qtd_dado_amarelo + qtd_dado_vermelho) > 0:
        random = randint(0, 2)
        if random == 0:
            if qtd_dado_verde > 0:
                tubo.append(dadoVerde)
                qtd_dado_verde -= 1
        elif random == 1:
            if qtd_dado_amarelo > 0:
                tubo.append(dadoAmarelo)
                qtd_dado_amarelo -= 1
        elif random == 2:
            if qtd_dado_vermelho > 0:
                tubo.append(dadoVermelho)
                qtd_dado_vermelho -= 1


def jogada(jogador_atual):
    mostraLinha()
    print("Jogada do jogador", indexJogadores[jogador_atual])
    time.sleep(2)
    inserirDadosNoTubo()  # Reinsere todos os dados no tubo
    mostraLinha()

    global indexTubo
    qtd_tiros = 0
    qtd_cerebros = 0
    lancamento = []  # lista de dados para serem lançados
    resultados = []  # os resultados dos dados que foram lançados (c, p, t)
    qtd_passos = []  # os dados cujos resultado foram 'passos'

    while True:
        lancamento.clear()  # limpa a lista de lançamentos
        resultados.clear()  # limpa a lista de resultados

        mostraLinha()
        # Checa se já existem dados com resultado "passos" na mesa
        # Se houver adiciona na lista de dados a serem lançados
        if len(qtd_passos) > 0:
            for dado in qtd_passos:
                lancamento.append(dado)
        qtd_passos.clear()  # limpa a lista de passos após adicioná-los na lista de lançamento(mão)

        print("Pegando 3 dados para lançar...")
        time.sleep(1.5)
        mostraLinha()

        # Se não houver quantidade suficiente de dados na mesa para ser lançado
        # Pega a quantidade faltante do tubo
        if len(lancamento) < 3:
            qtd_dados_pegar_do_tubo = 3 - len(lancamento)
            if indexTubo + qtd_dados_pegar_do_tubo >= len(tubo):  # se não houver dados suficientes na mesa e no tubo
                lancamento.clear()  # cancela o lançamento
                inserirDadosNoTubo()  # coloca todos os dados novamente no tubo
                qtd_dados_pegar_do_tubo = 3  # agora todos os dados serão pegos do tubo

            for dado in range(0, qtd_dados_pegar_do_tubo):
                lancamento.append(tubo[indexTubo])
                indexTubo += 1
        mostraLinha()

        print("A cor do primeiro dado é", lancamento[0][0], ", a cor do segundo dado é", lancamento[1][0],
              ", a cor do terceiro dado é", lancamento[2][0])
        time.sleep(2.5)
        mostraLinha()

        print("Jogando os dados...")
        time.sleep(1)
        for dado in lancamento:
            resultado = dado[randint(1, 6)]  # escolhe um lado aleatorio do dado
            if resultado == p:  # se o resultado for 'passos'
                qtd_passos.append(dado)  # adiciona na lista de dados com 'passos' que estão na mesa
            elif resultado == e:  # se o resultado for 'tiro'
                if qtd_tiros < 2:  # checa se o jogador já não tomou dois tiros
                    qtd_tiros += 1  # se não, incrementa a quantidade de tiros tomados
                else:  # se sim, este foi o terceiro tiro e então o jogador perde a vez
                    print("Você levou 3 tiros, perdeu a vez e não pontuou nessa rodada")
                    time.sleep(4)
                    return False
            else:  # se o resultado for 'cérebro'
                # incrementa a quantidade de cerebros obtidos nessa rodada
                qtd_cerebros += 1

                if jogadores[indexJogadores[jogador_atual]] + qtd_cerebros == 13:  # checa se o jogador ganhou
                    print("Você conseguiu comer 13 cérebros! Parabéns, você ganhou!")
                    time.sleep(4)
                    return True

            resultados.append(resultado)  # por fim, adiciona o resultado na lista de resultados

        mostraLinha()
        print('O resultado do primeiro dado foi \"' + resultados[0].capitalize() + "\".\n" +
              "O resultado do segundo dado foi \"" + resultados[1].capitalize() + "\".\n" +
              "O resultado do terceiro dado foi \"" + resultados[2].capitalize() + "\".\n")
        mostraLinha()
        time.sleep(1.5)

        while True:
            input_usuario = input(
                f'Zumbi {indexJogadores[jogador_atual]}, DESEJA JOGAR NOVAMENTE? '
                f'\n1-SIM\t2-NÃO\t3-VER PONTOS\n'.upper(), )
            if input_usuario == "1":  # se sim, reinicia o loop de jogada
                break
            elif input_usuario == "2":  # se não,
                # adciona os cérebros a pontuação do jogador
                jogadores[indexJogadores[jogador_atual]] += qtd_cerebros
                mostraLinha()
                print(f"Você consumiu {qtd_cerebros} cérebro(s) nessa rodada. "
                      f"Sua pontuação atual é {jogadores[indexJogadores[jogador_atual]]}")
                mostraLinha()
                return False  # retorna para jogoStart() e passa para o próximo jogador

            elif input_usuario == "3":  # mostra a quantidade de pontos (cérebros) do jogador
                mostraLinha()
                print(f"Você possui {jogadores[indexJogadores[jogador_atual]]} pontos")
                print(f"Você consumiu {qtd_cerebros} cérebros nessa rodada")
                print(f'No momento há {len(qtd_passos)} "passos" na mesa')
                print(f"Nessa rodada você tomou {qtd_tiros} tiro(s)")
                time.sleep(2)
                mostraLinha()
            else:
                print("Valor inválido, insira um valor correto:")


def mostraLinha():
    print('--' * 30)


iniciar()
