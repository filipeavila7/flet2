import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Definir as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Define as dimensões da janela do jogo
largura_janela = 600
altura_janela = 400

# Cria a janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da Cobrinha')

# Define o relógio para controlar o FPS
clock = pygame.time.Clock()

# Define o tamanho da cobrinha e a velocidade
tamanho_celula = 10
velocidade = 15

# Fonte para o placar
fonte_estilo = pygame.font.SysFont("bahnschrift", 25)

# Função para exibir o placar
def exibir_placar(pontos):
    texto = fonte_estilo.render("Pontuação: " + str(pontos), True, preto)
    janela.blit(texto, [0, 0])

# Função principal do jogo
def jogo():
    fim_de_jogo = False
    game_over = False

    # Posições iniciais da cobrinha
    x1 = largura_janela / 2
    y1 = altura_janela / 2

    # Posições iniciais do movimento da cobrinha
    x1_mover = 0
    y1_mover = 0

    # Cria o corpo da cobrinha
    corpo_cobrinha = []
    comprimento_cobrinha = 1

    # Geração de comida aleatória
    comida_x = round(random.randrange(0, largura_janela - tamanho_celula) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_janela - tamanho_celula) / 10.0) * 10.0

    # Laço principal do jogo
    while not fim_de_jogo:

        while game_over:
            janela.fill(azul)
            mensagem_game_over = fonte_estilo.render("Game Over! Pressione C para Jogar Novamente ou Q para Sair", True, vermelho)
            janela.blit(mensagem_game_over, [largura_janela / 6, altura_janela / 3])
            exibir_placar(comprimento_cobrinha - 1)
            pygame.display.update()

            # Evento de pressionar teclas após game over
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_de_jogo = True
                    game_over = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_de_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        # Detecta eventos de pressionamento de teclas
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mover = -tamanho_celula
                    y1_mover = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mover = tamanho_celula
                    y1_mover = 0
                elif evento.key == pygame.K_UP:
                    y1_mover = -tamanho_celula
                    x1_mover = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mover = tamanho_celula
                    x1_mover = 0

        # Verifica se a cobrinha bateu nas paredes
        if x1 >= largura_janela or x1 < 0 or y1 >= altura_janela or y1 < 0:
            game_over = True

        # Atualiza a posição da cobrinha
        x1 += x1_mover
        y1 += y1_mover
        janela.fill(azul)

        # Desenha a comida
        pygame.draw.rect(janela, verde, [comida_x, comida_y, tamanho_celula, tamanho_celula])

        # Atualiza o corpo da cobrinha
        corpo_cobrinha.append([x1, y1])
        if len(corpo_cobrinha) > comprimento_cobrinha:
            del corpo_cobrinha[0]

        # Verifica se a cobrinha bateu nela mesma
        for segmento in corpo_cobrinha[:-1]:
            if segmento == [x1, y1]:
                game_over = True

        # Desenha a cobrinha
        for segmento in corpo_cobrinha:
            pygame.draw.rect(janela, preto, [segmento[0], segmento[1], tamanho_celula, tamanho_celula])

        exibir_placar(comprimento_cobrinha - 1)

        pygame.display.update()

        # Verifica se a cobrinha comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_janela - tamanho_celula) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_janela - tamanho_celula) / 10.0) * 10.0
            comprimento_cobrinha += 1

        # Controla a velocidade do jogo
        clock.tick(velocidade)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
