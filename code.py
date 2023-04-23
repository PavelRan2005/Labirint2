from pygame import*

display.set_caption('Моя первая игра')
window = display.set_mode((800, 600))
background = transform.scale(image.load('city.png'), (800, 600))

class Card(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

class Pic(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

GREEN = (0,255,0)
w = 700
h = 500
player1 = Card(80,80,100,150,GREEN)
player2 = Pic('kik.png',200,200,200,250)

run = True
while run:
    time.delay(50)
    window.blit(background, (0,0))
    player1.draw()
    player2.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
