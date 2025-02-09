import pygame, random

pygame.init()

screen = pygame.display.set_mode([800, 600])

mousedown = False
Fixed_Update = True
clock = pygame.time.Clock()
pic = pygame.image.load('smile.bmp')

sprite_list = pygame.sprite.Group()

class Smiley(pygame.sprite.Sprite):
    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)

        self.image = pic
        self.scale = random.randint(10, 100)  # Делаем scale float
        
        # Умножаем размеры изображения на scale
        scaled_width = int(pic.get_width() * self.scale/ 100.0 ) 
        scaled_height = int(pic.get_height() * self.scale/ 100.0 )
        
        self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect(center=pos)  # Устанавливаем центр прямоугольника
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        # Проверяем столкновения со стенками экрана, используя rect.left, rect.right, rect.top, rect.bottom
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.xvel = -self.xvel
        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.yvel = -self.yvel

while Fixed_Update:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fixed_Update = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    if mousedown:
        new = Smiley(pygame.mouse.get_pos(), random.randint(-5, 5), random.randint(-5, 5))
        sprite_list.add(new)

    screen.fill((0, 0, 0))
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    clock.tick(60) # Ограничение FPS

pygame.quit()
