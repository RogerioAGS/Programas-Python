# 0. Criar uma instalação Desktop ------------------------------------

# PASSO 1: Digitar o seguinte código comentado abaixo:

# Importa os módulos os (para interagir com o sistema operacional) e 
# sys (para acessar variáveis e funções do interpretador Python).
import os, sys  

# Obtém o caminho completo do diretório onde o script está sendo executado e armazena em dirpath.
dirpath = os.getcwd()  

# Adiciona o diretório atual ao caminho de busca do Python. Isso permite que o Python encontre módulos 
# localizados no mesmo diretório que o script. No caso as subpastas com os assets
sys.path.append(dirpath)  

# Verifica se o script está sendo executado como um executável compilado 
# (por exemplo, usando PyInstaller).
if getattr(sys, "frozen", False):  
    os.chdir(sys._MEIPASS)  # Se estiver compilado, muda o diretório de trabalho atual 
                            # para o diretório onde os arquivos do aplicativo foram extraídos.


# PASSO 2: Após a inserção do código acima instalar o pyinstaller no terminal com o comando: 
#  - pip install pyinstaller    


# PASSO 3: Executar o seguinte comando no terminal (o parametro -F é para colocar em um único arquivo):
#  - pyinstaller -F main.py

# PASSO 4: Abrir o arquivo main.spec e alterar o item: datas=[("data", "data")] como mostrado abaixo
#  a = Analysis(
#     ['main.py'],
#     pathex=[],
#     binaries=[],
#     datas=[("data", "data")],
#     hiddenimports=[],
#     hookspath=[],
#     hooksconfig={},
#     runtime_hooks=[],
#     excludes=[],
#     noarchive=False,
#     optimize=0,
# )

# PASSO 5: Executar o seguinte comando no terminal:
#  - pyinstaller main.spec

# PASSO 6: Verificar o arquivo executavel na pasta dist

#########################################################################################################
# Pygame:
#   - Instalar a biblioteca no terminal: pip install pygame


# 1. IMPORTS -------------------------------------------------------------------
import pygame
import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot
from pumpkin import Pumpkin


# 2. INICIALIZAÇÃO--------------------------------------------------------------

# 2.1 Iniciar Pygame
pygame.init()

# 2.2 Iniciar a janela com a configuração de resolução de 840x480

# 2.2.1 Constantes de largura e altura de tela
LARGURA_TELA = 840
ALTURA_TELA = 480

# 2.2.2 Criar a janela
display = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])

# 2.2.3 Preencher o fundo da janela com uma cor RGB
display.fill([66, 135, 245])
# 2.2.4 Preencher o fundo da janela com uma cor em HEX
# display.fill("#4287f5")

# 2.2.5 Mudar o título da janela
pygame.display.set_caption("Game SENAI - Python 315")

# 2.2.6 Carregar a imagem do icone e mudar o icone da janela
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)


# 3. ELEMENTOS DE TELA ---------------------------------------------------------

# 3.1 Personagens

# Criar um grupo de imagens para inserir todas as imagens e desenhar elas de uma 
# única vez 
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()


# 3.2 Fontes ------------------------------------------------------------------
score_font = pygame.font.Font("data/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("data/Pixeltype.ttf", 200)

# 3.3 Música ----------------------------------------------------------
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1)  # -1 para ser um loop infinito

# 3.4 Som (SFX) ------------------------------------------------------
attack = pygame.mixer.Sound("data/magic1.wav")

# 4. VARIAVEIS GLOBAIS ---------------------------------------------------------
gameLoop = True
gameOver = False

timer = 20
pontos = 0

numSetupFase = 1
numfase = 1

vidas = 3

# 4.1 Criar um clock para ajustar os frames por segundo (fps)
clock = pygame.time.Clock()


# 5. FUNÇÃO PRINCIPAL ----------------------------------------------------------
def main():

    global gameLoop
    global gameOver
    global timer
    global pontos
    global numSetupFase
    global numfase
    global vidas
   

    while gameLoop:
        # Clock de 60fps
        clock.tick(60)


        if numSetupFase == 1:
            # Criar um cenário (background) para o fantasma
            bg = pygame.sprite.Sprite(objectGroup)
            bg.image = pygame.image.load("data/background.jpg")
            bg.image = pygame.transform.scale(bg.image, [840, 480])
            bg.rect = bg.image.get_rect()

            # Criar um objeto da Classe Ghost e coloco no grupo objectGroup
            ghost = Ghost(objectGroup)

            numSetupFase = 0
            numfase = 1

        if numSetupFase == 2:
            # Criar um cenário (background) para o fantasma
            bg = pygame.sprite.Sprite(objectGroup)
            bg.image = pygame.image.load("data/bg_fase2.jpg")
            bg.image = pygame.transform.scale(bg.image, [840, 480])
            bg.rect = bg.image.get_rect()

            # Criar um objeto da Classe Ghost e coloco no grupo objectGroup
            ghost = Ghost(objectGroup)

            numSetupFase = 0
            numfase = 2

        # Loop de Eventos - Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN: # Evento Tiros
                if event.key == pygame.K_SPACE:
                    if Shoot.numTiros < 5:
                        newShoot = Shoot(objectGroup, shootGroup)
                        newShoot.rect.center = ghost.rect.center
                        attack.play()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Shoot.numTiros < 5:
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = ghost.rect.center
                    attack.play()

        if not gameOver:
                
            
            timer += 1

            # Criar varios morcegos
            if timer > 30 and numfase == 1:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup) 

            # Criar varios morcegos e aboboras
            if timer > 30 and numfase == 2:
                timer = 0
                if random.random() < 0.45:
                    newBat = Bat(objectGroup, batGroup) 
                if random.random() < 0.25:
                    newPumpkin = Pumpkin(objectGroup, batGroup) 

            # Colisao dos Morcegos com o Fantasma
            colisao = pygame.sprite.spritecollide(
                ghost,
                batGroup,
                True,
                pygame.sprite.collide_mask
            )

            if colisao:
                vidas -= 1
                
            if vidas == 0:
                gameOver = True

            # Colisao do tiro com o morcego
            tiros = pygame.sprite.groupcollide(
                shootGroup,
                batGroup,
                True,
                True,
                pygame.sprite.collide_mask
            )

            if tiros:
                pontos += 1
                Shoot.subtrairTiros()

                if pontos ==  10:
                    ghost.kill()
                    numSetupFase = 2

            # Atualizar a posição do objetos
            objectGroup.update()

        # Desenhar na tela
        objectGroup.draw(display)

        # Inserir a pontuação na tela
        score_render = score_font.render(f"Score: {pontos}", False, "White")
        display.blit(score_render, (650,50))

        # Vidas
        score_render = score_font.render(f"Life: {vidas}", False, "White")
        display.blit(score_render, (50,50))

        # Inserir a mensagem GAME OVER na tela
        if gameOver:
            gameOverMsg = gameOver_font.render("GAME OVER", False, "White")
            display.blit(gameOverMsg, (100,150))

        # Atualização da tela
        pygame.display.update()




if __name__ == "__main__":
    main()