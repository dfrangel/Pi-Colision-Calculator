# main.py
import pygame
import sys
from blocos import Bloco, colide_blocos 

pygame.init()
pygame.font.init()
fonte_padrao = pygame.font.SysFont("Arial", 36)

LARGURA = 1200
ALTURA = 600

# CONVERSÃO PARA FLOAT AQUI:
peso1 = float(input("Digite o peso do bloco 1: "))
vel1 = float(input("Digite a velocidade do bloco 1: "))
peso2 = float(input("Digite o peso do bloco 2: "))

# Criando os objetos
bloco1 = Bloco(peso1, vel1, 100)
bloco2 = Bloco(peso2, 0, (LARGURA - 600))

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulador de Colisão")

COR_FUNDO = (240, 240, 240)
COR_TEXTO = (30, 30, 30)
relogio = pygame.time.Clock()
contador_colisoes = 0
rodando = True

# --- LOOP PRINCIPAL ---
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False

    # --- 2. ATUALIZAÇÃO DA LÓGICA ---
    # Verifica a colisão (AABB - Axis-Aligned Bounding Box básico)
    # Se a borda direita do bloco 1 passa da esquerda do 2, e vice-versa:
    if bloco1.x + bloco1.tam >= bloco2.x and bloco1.x <= bloco2.x + bloco2.tam:
        colide_blocos(bloco1, bloco2)
        contador_colisoes += 1 # Conta a batida entre os blocos
        
        # Um pequeno "empurrão" para evitar que fiquem colados no mesmo frame
        bloco1.x += bloco1.vel
        bloco2.x += bloco2.vel

    # Atualiza as posições e conta batidas na parede direita
    # Se o update retornar True, quer dizer que bateu na borda direita
    if bloco1.update(LARGURA):
        contador_colisoes += 1
        
    if bloco2.update(LARGURA):
        contador_colisoes += 1

    # --- 3. RENDERIZAÇÃO ---
    tela.fill(COR_FUNDO)
    
    pygame.draw.rect(tela, (0, 0, 240), pygame.Rect(bloco1.x, ALTURA/2 - 40, bloco1.tam, bloco1.tam))
    pygame.draw.rect(tela, (240, 0, 0), pygame.Rect(bloco2.x, ALTURA/2 - 40, bloco2.tam, bloco2.tam))

    # Renderiza e desenha o contador na tela
    texto_surface = fonte_padrao.render(f"Colisões: {contador_colisoes}", True, COR_TEXTO)
    tela.blit(texto_surface, (20, 20))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()