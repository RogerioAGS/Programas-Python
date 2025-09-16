import pygame

class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        # Carregar a imagem para uso
        self.image = pygame.image.load("data/ghost-x4.gif")
        # Redimensionar a imagem para completar nosso retângulo em 100%
        self.image = pygame.transform.scale(self.image, [100, 100])
        # Posicionando e dimensionando o retangulo na tela
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speedX = 0
        self.accelerationX = 0.1

        self.speedY = 0
        self.accelerationY = 0.1

    def update(self, *args):

        # Evento Movimentação
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.speedY += self.accelerationY
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speedY -= self.accelerationY
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.speedX += self.accelerationX
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.speedX -= self.accelerationX
        else:
            self.speedY *= 0.95
            self.speedX *= 0.95

        self.rect.y += self.speedY
        self.rect.x += self.speedX

        # Limite de Tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speedY = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedX = 0
        elif self.rect.right > 840:
            self.rect.right = 840
            self.speedX = 0