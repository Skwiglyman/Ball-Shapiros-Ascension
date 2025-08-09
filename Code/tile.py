import pygame
from gameData import *
from settings import *
from debug import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, Data):
        super().__init__()

        self.image = pygame.image.load(Data["Graphic"]).convert_alpha()
        self.pos = [x + SCREEN_WIDTH*0.25, y]
        self.rect = self.image.get_rect(topleft = (x + SCREEN_WIDTH*0.25, y))
    
    def update(self, shift = 0):
        self.rect.top += shift

class Decoration(Tile):
    def __init__(self, x, y, Data):
        super().__init__(x, y, Data)

class layoutTile(Tile):
    def __init__(self, x, y, Data):
        super().__init__(x, y, Data)
        self.YBounce = Data["YBounce"]
        self.XBounce = Data["XBounce"]
        self.Friction = Data["Friction"]

class Slime(Tile):
    def __init__(self, x, y, Data):
        super().__init__(x, y, Data)
        self.YBounce = Data["YBounce"]
        self.XBounce = Data["XBounce"]
        self.Friction = Data["Friction"]

class Slope(Tile):
    def __init__(self, x, y, Data):
        super().__init__(x, y, Data)

        self.Facing = Data["Facing"]

class Combined(pygame.sprite.Sprite):
    def __init__(self, sprites):
        super().__init__()
        # Combine the rects of the separate sprites.
        self.rect = sprites[0].rect.copy()
        for sprite in sprites[1:]:
            self.rect.union_ip(sprite.rect)

        # Create a new transparent image with the combined size.
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # Now blit all sprites onto the new surface.
        for sprite in sprites:
            self.image.blit(sprite.image, (sprite.rect.x-self.rect.left, sprite.rect.y-self.rect.top))
        self.pos = [self.rect.x, self.rect.y]

class Dash_Crystal(Tile):
    def __init__(self, x, y, Data):
        super().__init__(x, y, Data)
        self.start = 0
        self.end = 120
        self.isAlive = True
    
    def reset(self):
        # pygame.draw.circle(display_surface, (174, 239, 90),  (self.pos[0] + 16, self.pos[1] + 16), round(self.radius), 10)
        self.start += 1

        if self.start >= self.end:
            self.isAlive = True

    def draw(self, display_surface):
        if self.isAlive:
            display_surface.blit(self.image, self.rect)

ClassDict = {"Layout": layoutTile, "Slopes": Slope, "D_Crystal": Dash_Crystal, 
"Slime": Slime, "Decoration": Decoration, "Decoration2": Decoration, "Decoration3": Decoration}