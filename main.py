
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

graph = {
    (300,500): [(500,500),(100,500),(300,300)],
    (500,500): [(300,500)],
    (100,500): [(300,500),(100,300)],
    (100,300): [(100,500),(100,100)],
    (300,300): [(300,500),(500,300),(300,100)],
    (500,300): [(300,300),(500,100)],
    (100,100): [(100,300),(300,100)],
    (300,100): [(300,300),(100,100)],
    (500,100): [(500,300)]
}
#
move = None

player_position = (300,500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                move = 'left'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                move = "right"
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
                move = 'up'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                print("down")
                move = 'down'

    # Redraw the screen to erase previous drawings
    screen.fill((0, 0, 0))

    # Draw the nodes
    for node, data in graph.items():
        pygame.draw.circle(screen, (255, 255, 255), node, 20)
        for neighbor in graph[node]:
            pygame.draw.line(screen, (255, 255, 255), node, neighbor)
    
    # Get the adjacent nodes for the current player position
    adjacent_nodes = graph[player_position]
   
    if move == 'up':
        x, y = player_position
        new_y = y - 200
        if (x, new_y) in adjacent_nodes:
            player_position  = (x, new_y)
            move = None
    if move == "down":
        x, y = player_position
        new_y = y + 200
        if (x, new_y) in adjacent_nodes:
            player_position  = (x, new_y)
            move = None
        
    if move == "left":
        x, y = player_position
        new_x = x - 200
        if (new_x, y) in adjacent_nodes:
            player_position = (new_x, y) 
            move = None

    if move == "right":
        x, y = player_position
        new_x = x + 200
        if (new_x, y) in adjacent_nodes:
            player_position = (new_x, y) 
            move = None

    

    # Draw the current player position
    pos = player_position
    pygame.draw.circle(screen, (255, 0, 0), pos, 10)
    pygame.display.flip()
    pygame.time.delay(500)

