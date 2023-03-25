import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1000,800])
base_font = pygame.font.Font(None,32)
user_text = ''
prompt_text = 'Comandos do Fogao'
diagram = pygame.image.load('images/diagrama.png').convert_alpha()

input_rect =  pygame.Rect(30,500, 215,32)
color = pygame.Color('lightskyblue3')

# --STOVEN-- #
stoven_height = 300
stoven_weight = 300
stoven_color = pygame.Color('gray')
mouth_color_1 = pygame.Color('orange')
mouth_color_2 = pygame.Color('orange')
mouth_color_3 = pygame.Color('orange')
mouth_color_4 = pygame.Color('orange')

q0 = pygame.Color('black')
q1 = pygame.Color('black')
q2 = pygame.Color('black')
q3 = pygame.Color('black')
q4 = pygame.Color('black')
q5 = pygame.Color('black')
q6 = pygame.Color('black')
q7 = pygame.Color('black')
q8 = pygame.Color('black')
    
while True: # loop infinito do jogo

    for event in pygame.event.get(): #event eh so um index, o que importa e o pygame.event que define qual tipo de evento esta acontecendo dentro do "jogo"
        if event.type == pygame.QUIT: #evento de sair do jogo
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN: #evento do jogador teclar algo
            if event.key == pygame.K_BACKSPACE: #evento do jogador apertar a tecla apagar
                user_text = user_text[:-1] #apagando um index da string user_text
            
            elif event.key == pygame.K_RETURN:
                match user_text:
                    case '0000': #todas as bocas desligadas 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '1000': # boca 1 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '0100': # boca 2 ligada 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '0010': # boca 3 ligada 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '0001': # boca 4 ligada \
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '1100': # boca 1 e 2 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '1010': # boca 1 e 3 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '1001': # boca 1 e 4 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '0110': # boca 2 e 3 ligada 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '0101': # boca 2 e 4 ligada 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '0011': # boca 3 e 4 ligada 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '1110': # boca 1,2,3 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('orange')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('green')
                        q8 = pygame.Color('black')
                    case '0111': # boca 2,3,4 ligada 
                        mouth_color_1 = pygame.Color('orange')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('green')
                        q2 = pygame.Color('black')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '1011': # boca 1,3,4 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('orange')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('green')
                        q4 = pygame.Color('black')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '1101': # boca 1,2,4 ligada 
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('orange')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('green')
                        q6 = pygame.Color('black')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                    case '1111': # todas as bocas ligadas  
                        mouth_color_1 = pygame.Color('green')
                        mouth_color_2 = pygame.Color('green')
                        mouth_color_3 = pygame.Color('green')
                        mouth_color_4 = pygame.Color('green')

                        q0 = pygame.Color('green')
                        q1 = pygame.Color('black')
                        q2 = pygame.Color('green')
                        q3 = pygame.Color('black')
                        q4 = pygame.Color('green')
                        q5 = pygame.Color('black')
                        q6 = pygame.Color('green')
                        q7 = pygame.Color('black')
                        q8 = pygame.Color('green')
                user_text = ''
            
            else:
                user_text += event.unicode #unicode eh o input do pygame, so isso mesmo
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color,input_rect,2) #caixa de texto
    pygame.draw.rect(screen,stoven_color, (150,100,stoven_weight,stoven_height)) # fogao
    screen.blit(diagram, (600, 100, 500, 500))

    pygame.draw.circle(screen,mouth_color_1, (200, 150) ,50)
    pygame.draw.circle(screen,mouth_color_2, (400, 150) ,50)
    pygame.draw.circle(screen,mouth_color_3, (200, 350) ,50)
    pygame.draw.circle(screen,mouth_color_4, (400, 350) ,50)
    pygame.draw.circle(screen,q0, (731, 175) ,45, width=7)

    pygame.draw.circle(screen,q1, (642, 295) ,45, width=7)
    pygame.draw.circle(screen,q2, (821, 295) ,45, width=7)
    
    pygame.draw.circle(screen,q3, (642, 437) ,45, width=7)
    pygame.draw.circle(screen,q4, (821, 437) ,45, width=7)

    pygame.draw.circle(screen,q5, (642, 597) ,45, width=7)
    pygame.draw.circle(screen,q6, (821, 597) ,45, width=7)

    pygame.draw.circle(screen,q7, (642, 747) ,45, width=5)
    pygame.draw.circle(screen,q8, (821, 747) ,45, width=5)


    # O conteudo do texto e como ele sera renderizado! (funcao render -> renderizar como vai ser o programa)
    prompt_text_surface = base_font.render(prompt_text, True, (255,255,255))
    text_surface = base_font.render(user_text, True, (255,255,255))
    
    # O texto a ser usado e mostrando na tela (funcao blit -> mostrar na tela) 
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    screen.blit(prompt_text_surface, (input_rect.x, input_rect.y - 22))
    
    pygame.display.flip()
    clock.tick(60)
