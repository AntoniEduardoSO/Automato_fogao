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

        screen.blit(self.image, (30,200))

        
            
class Diagram(pygame.sprite.Sprite):
    def __init__(self, current_sprite):
        super().__init__()
        self.sprite = []

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
        

        screen.blit(self.image, (30, 650))


           


input = 0
i = 0


stoven = Stoven(i)

diagram = pygame.image.load('images/Diagram_0000.png')
diagram = pygame.transform.scale(diagram, (400,600))

base_font = pygame.font.Font(None,32)
user_text = ''
prompt_text = 'Comandos do Fogao'
# diagram = pygame.image.load('images/diagrama.png').convert_alpha()
stoven_rect = pygame.image.load('images/stoven_rect.png')
stoven_rect = pygame.transform.scale(stoven_rect, (300, 50))

input_rect =  pygame.image.load('images/rect_input.png')
input_rect = pygame.transform.scale(input_rect, (400,100))


sprite_KBACKSPACE = pygame.image.load('images/sprite_backspace.png')
sprite_KBACKSPACE = pygame.transform.scale(sprite_KBACKSPACE, (36,24))





    
while True: # loop infinito do jogo

    for event in pygame.event.get(): #event eh so um index, o que importa e o pygame.event que define qual tipo de evento esta acontecendo dentro do "jogo"
        if event.type == pygame.QUIT: #evento de sair do jogo
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN: #evento do jogador teclar algo
            if event.key == pygame.K_BACKSPACE: #evento do jogador apertar a tecla apagar
                user_text = user_text[:-1] #apagando um index da string user_text
            
            elif event.key == pygame.K_RETURN:
                match input:
                    case 1: #todas as bocas desligadas
                        stoven = Stoven(0)

                    case 2: # boca 1 ligada
                        stoven = Stoven(1)
                        
                    case 3: # boca 2 ligada
                        stoven = Stoven(2) 

                    case 4: # boca 3 ligada
                        stoven = Stoven(3)

                    case 5: # boca 4 ligada \
                        stoven = Stoven(4)

                    case 6: # boca 1 e 2 ligada
                        stoven = Stoven(5)

                    case 7: # boca 1 e 3 ligada
                        stoven = Stoven(6)

                    case 8: # boca 1 e 4 ligada
                        stoven = Stoven(7) 

                    case 9: # boca 2 e 3 ligada
                        stoven = Stoven(8)

                    case 10: # boca 2 e 4 ligada
                        stoven = Stoven(9)

                    case 11: # boca 3 e 4 ligada 
                        stoven = Stoven(10)

                    case 12: # boca 1,2,3 ligada 
                        stoven = Stoven(11)


                    case 13: # boca 2,3,4 ligada 
                        stoven = Stoven(12)

                    case 14: # boca 1,3,4 ligada 
                        stoven = Stoven(13)

                    case 15: # boca 1,2,4 ligada 
                        stoven = Stoven(14)

                    case 16: # todas as bocas ligadas 
                        stoven = Stoven(15) 

                user_text = ''
            
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

    
    
    

    screen.fill((71,25,93))
    # pygame.draw.rect(screen,color,input_rect,2) #caixa de texto
    screen.blit(stoven_rect, (30,40))
    screen.blit(stoven.image, (30,150))
    sprites = Sprite(input)
    screen.blit(diagram, (500, 50))

     
    
    pygame.display.flip()
    clock.tick(60)
