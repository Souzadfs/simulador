import pygame

# Inicializar o pygame
pygame.init()

# Inicializar o módulo de fontes
pygame.font.init()
font = pygame.font.Font(None, 36)  # Usar uma fonte padrão com tamanho 36

# Configurar a tela em modo tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()  # Obter largura e altura da tela
pygame.display.set_caption("Simulação de Pintura em Zig-Zag")

# Definir cor, tamanho e variáveis da bola
ball_color = (0, 0, 255)
ball_radius = 40  # Raio da bola
ball_x = ball_radius  # Iniciar a bola na borda esquerda
ball_speed_x = 5  # Velocidade horizontal da bola

# Variáveis de posição vertical
positions_y = [screen_height // 8 * i for i in range(8)]  # Cria uma lista com 8 posições verticais
current_y_index = 0  # Começa na posição superior
ball_y = positions_y[current_y_index]  # Define a posição inicial da bola

# Controle de movimento e visibilidade
moving = True  # Define se a bola está em movimento ou parada
visible = True  # Define se a bola está visível

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                moving = not moving  # Iniciar ou parar o movimento
            elif event.key == pygame.K_ESCAPE:
                running = False  # Sair do modo tela cheia
            elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                # Aumentar a velocidade mantendo a direção
                ball_speed_x += 1 if ball_speed_x > 0 else -1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                # Diminuir a velocidade mantendo a direção, com velocidade mínima de 1
                ball_speed_x = (abs(ball_speed_x) - 1) * (1 if ball_speed_x > 0 else -1)
            elif event.key == pygame.K_v:  # Alternar visibilidade com a tecla "V"
                visible = not visible  # Alternar visibilidade

    # Atualizar a posição da bola se o movimento estiver ativado
    if moving:
        ball_x += ball_speed_x

        # Verificar se a bola atinge as extremidades da tela
        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
            # Inverter a direção horizontal
            ball_speed_x = -ball_speed_x
            
            # Mover para a próxima posição vertical
            current_y_index += 1
            if current_y_index >= len(positions_y):
                pygame.time.delay(700)  # Pausa de 3 segundos antes de reiniciar
                current_y_index = 0  # Reiniciar do topo se atingir o fim das posições

            ball_y = positions_y[current_y_index]  # Atualiza a posição vertical

    # Preencher a tela com cinza
    screen.fill((169, 169, 169))  # Fundo cinza

    # Desenhar a bola se estiver visível
    if visible:
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Renderizar e desenhar o texto da velocidade na tela
    speed_text = font.render(f'Velocidade: {ball_speed_x}', True, (255, 255, 255))  
    screen.blit(speed_text, (20, screen_height - 50))  

    pygame.display.flip()
    clock.tick(200)  # Manter 200 FPS

pygame.quit()
