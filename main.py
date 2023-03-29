import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1000,800])



class Stoven(pygame.sprite.Sprite):
    def __init__(self, current_sprite):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Stoven_0000.png')) 
        self.sprites.append(pygame.image.load('images/Stoven_1000.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0100.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0010.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0001.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1100.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1010.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1001.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0110.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0101.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0011.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1110.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1101.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1011.png'))
        self.sprites.append(pygame.image.load('images/Stoven_0111.png'))
        self.sprites.append(pygame.image.load('images/Stoven_1111.png'))

        self.image = self.sprites[current_sprite]
        self.image = pygame.transform.scale(self.sprites[current_sprite], (400,500))           

        screen.blit(self.image, (30,180))

        
            
class Diagram(pygame.sprite.Sprite):
    def __init__(self, current_sprite):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Diagram_0000.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1000.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0100.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0010.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0001.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1100.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1010.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1001.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0110.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0101.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0011.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1110.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1101.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1011.png'))
        self.sprites.append(pygame.image.load('images/Diagram_0111.png'))
        self.sprites.append(pygame.image.load('images/Diagram_1111.png')) # 16
        
        self.image = self.sprites[current_sprite]
        self.image = pygame.transform.scale(self.sprites[current_sprite], (400,600))

        screen.blit(self.image, (550, 180))


class Sprite(pygame.sprite.Sprite):
    def __init__(self, current_sprite):
        super().__init__()
        self.sprites = []
        
        self.sprites.append(pygame.image.load('images/rect_input.png'))  # 0
        self.sprites.append(pygame.image.load('images/rect_input_0000.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1000.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0100.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0010.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0001.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1100.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1010.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1001.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0110.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0101.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0011.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1110.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1101.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1011.png'))
        self.sprites.append(pygame.image.load('images/rect_input_0111.png'))
        self.sprites.append(pygame.image.load('images/rect_input_1111.png')) # 16
        
        self.image = self.sprites[current_sprite]
        self.image = pygame.transform.scale(self.sprites[current_sprite], (400,100))
        
        screen.blit(self.image, (30, 680))

input_diagram = 0
input = 0
stoven = Stoven(input)
diagram = Diagram(input)


stoven_lettering = pygame.image.load('images/stoven_rect.png')
stoven_lettering = pygame.transform.scale(stoven_lettering, (400, 50))
diagram_lettering = pygame.image.load('images/diagram_rect.png')
diagram_lettering = pygame.transform.scale(diagram_lettering, (400, 50))
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (1000, 800))


input_rect =  pygame.image.load('images/rect_input.png')
input_rect = pygame.transform.scale(input_rect, (400,100))

while True: # loop infinito do jogo

    for event in pygame.event.get(): #event eh so um index, o que importa e o pygame.event que define qual tipo de evento esta acontecendo dentro do "jogo"
        if event.type == pygame.QUIT: #evento de sair do jogo
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN: #evento do jogador teclar algo
            if event.key == pygame.K_RETURN:
                match input:
                    case 1: #todas as bocas desligadas
                        stoven = Stoven(0)
                        diagram = Diagram(0)
                        input_diagram = 0

                    case 2: # boca 1 ligada
                        stoven = Stoven(1)
                        diagram = Diagram(1)
                        input_diagram = 1
                        
                    case 3: # boca 2 ligada
                        stoven = Stoven(2)
                        diagram = Diagram(2)
                        input_diagram = 2

                    case 4: # boca 3 ligada
                        stoven = Stoven(3)
                        diagram = Diagram(3)
                        input_diagram = 3

                    case 5: # boca 4 ligada \
                        stoven = Stoven(4)
                        diagram = Diagram(4)
                        input_diagram = 4

                    case 6: # boca 1 e 2 ligada
                        stoven = Stoven(5)
                        diagram = Diagram(5)
                        input_diagram = 5

                    case 7: # boca 1 e 3 ligada
                        stoven = Stoven(6)
                        diagram = Diagram(6)
                        input_diagram = 6

                    case 8: # boca 1 e 4 ligada
                        stoven = Stoven(7)
                        diagram = Diagram(7)
                        input_diagram = 7

                    case 9: # boca 2 e 3 ligada
                        stoven = Stoven(8)
                        diagram = Diagram(8)
                        input_diagram = 8

                    case 10: # boca 2 e 4 ligada
                        stoven = Stoven(9)
                        diagram = Diagram(9)
                        input_diagram = 9

                    case 11: # boca 3 e 4 ligada 
                        stoven = Stoven(10)
                        diagram = Diagram(10)
                        input_diagram = 10

                    case 12: # boca 1,2,3 ligada 
                        stoven = Stoven(11)
                        diagram = Diagram(11)
                        input_diagram = 11

                    case 13: # boca 2,3,4 ligada 
                        stoven = Stoven(12)
                        diagram = Diagram(12)
                        input_diagram = 12

                    case 14: # boca 1,3,4 ligada 
                        stoven = Stoven(13)
                        diagram = Diagram(13)
                        input_diagram = 13

                    case 15: # boca 1,2,4 ligada 
                        stoven = Stoven(14)
                        diagram = Diagram(14)
                        input_diagram = 14

                    case 16: # todas as bocas ligadas 
                        stoven = Stoven(15)
                        diagram = Diagram(15)
                        input_diagram = 15
            
            else:
                if event.key == pygame.K_DOWN:
                    if input < 1:
                        input = 16
                    else:
                         input-=1
                    

                    sprite= Sprite(input)
                
                elif event.key == pygame.K_UP:
                    if input > 15:
                        input = 1
                    else:
                        input += 1
                    
                    sprites = Sprite(input)

    
    
    

    # pygame.draw.rect(screen,color,input_rect,2) #caixa de texto
    screen.blit(background, (0,0))
    screen.blit(stoven_lettering, (30,130))
    screen.blit(diagram_lettering, (550,130))
    stoven = Stoven(input_diagram)
    sprites = Sprite(input)
    diagram = Diagram(input_diagram)
    
    
    pygame.display.flip()
    clock.tick(60)
