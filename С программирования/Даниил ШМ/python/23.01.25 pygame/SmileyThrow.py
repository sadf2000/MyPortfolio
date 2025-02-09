import pygame, random

pygame.init()

screen = pygame.display.set_mode([800, 600])

clock = pygame.time.Clock()
pic = pygame.image.load('GamePython/smile.bmp')

sprite_list = pygame.sprite.Group()

class Smiley(pygame.sprite.Sprite):
    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)

        self.image = pic
        self.scale = random.randint(10, 100)
        
        # Масштабируем изображение
        scaled_width = int(pic.get_width() * self.scale / 100.0)
        scaled_height = int(pic.get_height() * self.scale / 100.0)
        
        self.image = pygame.transform.scale(self.image, (scaled_width, scaled_height))
        self.rect = self.image.get_rect(center=pos)
        self.xvel = xvel 
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        # Проверяем столкновения со стенками экрана
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.xvel = -self.xvel * 0.95
        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.yvel = -self.yvel * 0.95

mouseType = 0
Fixed_Update = True
mousebutton = False
while Fixed_Update:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fixed_Update = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseType = 1
            if event.button == 3:
                mouseType = 2
        else:
            mouseType = 0
        
    if mouseType > 0:
        if mouseType == 1:  # Левая кнопка
                new = Smiley(event.pos, random.randint(-5, 5), random.randint(-5, 5))
                sprite_list.add(new)
        elif mouseType == 2:  # Правая кнопка
            pos = event.pos
            for sprite in sprite_list:
                 if sprite.rect.collidepoint(pos):
                    sprite_list.remove(sprite)  # Удаляем смайлик, если кликнули по нему
                    break
    screen.fill((0, 0, 0))
    sprite_list.update()
    sprite_list.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
