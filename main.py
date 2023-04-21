
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600, 600))


#level 1 graph
graph = {
    (200, 300): [(300, 300), (100, 300), (200, 200), (200, 400)],
    (300, 300): [(200, 300)],
    (100, 300): [(200, 300), (100, 200)],
    (100, 200): [(100, 300), (100, 100)],
    (200, 200): [(300, 200), (200, 100),(200,300)],
    (300, 200): [(300, 100),(200,200)],
    (100, 100): [(200, 100),(100,200)],
    (200, 100): [(200, 200), (100, 100)],
    (300, 100): [(300, 200)],
    (200, 400): [(200, 300), (300, 400),(200,500)],
    (300, 400): [(200, 400), (400, 400), (300, 500)],
    (300, 500): [(300, 400), (400, 500),(200,500)],
    (400, 400): [(300, 400), (400, 500),(500,400),(400,300)],
    (400, 500): [(400, 400), (300, 500),(500,500)],
    (400, 300): [(400, 400),(400,200)], 
    (200, 500): [(200, 400), (300, 500)],
    (400, 200): [(400, 300),(400,100)],
    (500, 300): [(500,400)],
    (500, 400): [(400, 400),(500,300)],
    (500, 500): [(400, 500)],
    (400, 100): [(400, 200),(500,100)],
    (500, 100): [(400, 100)],
}

#level 2 graph
graph2 = {
    (100,100):[(100,200),(200,100)],
    (100,200):[(100,100),(100,300)],
    (200,100):[(100,100)],
    (100,300):[(100,200)]

}

level_maps = {1:graph,2:graph2}

level_positions = {1:[(300,500),(500,100),(100,100)],2:[(),(),()]}


def draw_level(level):
    graph = level_maps[level]
    screen.fill((0, 0, 0))
    for node, data in graph.items():
                pygame.draw.circle(screen, (255, 255, 255), node, 20)
                for neighbor in graph[node]:
                    pygame.draw.line(screen, (255, 255, 255), node, neighbor,20)

#queue functions
def priority_dequeue(queue):
  greatest  = 9999999
  for i in range(len(queue)):
    if queue[i][1] < greatest:
      index = i
  item = queue.pop(index)
  return item

def enqueue(queue,item):
  queue.append(item)


#dijkstra algorithm
def getShortestPath(graph,src,end):
    node_cost = {}
    track_parents = {}
    visited = {}
    priority_q = []
    infinity = 999999

    for node in graph:
        node_cost[node] = 999999 
        track_parents[node] = None
        visited[node] = False
  
    visited[src] = True
    node_cost[src] = 0
    priority_q.append((src,0))

    while priority_q:
        node_tuple = priority_dequeue(priority_q)
        current_node = node_tuple[0]
        weight_node = node_tuple[1]
        visited[current_node] == True

        for neighbour in graph[current_node]:
            if visited[neighbour] == False:
                new_cost = weight_node + 1
            if new_cost < node_cost[neighbour]:
                node_cost[neighbour] = new_cost
                track_parents[neighbour] = current_node
                enqueue(priority_q, (neighbour, new_cost))

  
    edges = []

    current_node = end
    while current_node != src:
        parent_node = track_parents[current_node]
        edges.append((parent_node, current_node))
        current_node = parent_node

    edges.reverse()
    if edges == []:
        return -1
    return edges

#win_screen screen
def win_screen():
    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial", 25)
    txt = font.render("You Win", True, (255,255,255))
    text_rect = txt.get_rect(center= (300,300))
    screen.blit(txt, text_rect)
    pygame.display.update()

#game_over screen
def lose_screen():
    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial", 25)
    txt = font.render("You Lose", True, (255,255,255))
    text_rect = txt.get_rect(center= (300,300))
    screen.blit(txt, text_rect)
    pygame.display.update()

#start_menu screen
def start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Chaser Game', True, (255, 255, 255))
    start_button = font.render('Press "space" to start', True, (255, 255, 255))
    screen.blit(title, (600/2 - title.get_width()/2, 600/2 - title.get_height()/2))
    screen.blit(start_button, (600/2 - start_button.get_width()/2, 600/2 + start_button.get_height()/2))
    pygame.display.update()

game_state = "start_menu"

max_level = 1


#main loop
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
    if game_state == 'start_menu':
        start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            level = 1
            player_position = level_positions[level][0]
            winner_position = level_positions[level][1]
            chaser_position = level_positions[level][2]
            flag = False
            move = None
            game_state = "game"
    if game_state == 'game':
        # Draw the nodes
        draw_level(level)

        # Get the adjacent nodes for the current player position
        adjacent_nodes = level_maps[level][player_position]

        #player traversal
        if move == 'up':
            x, y = player_position
            new_y = y - 100
            if (x, new_y) in adjacent_nodes:
                player_position  = (x, new_y)
                move = None
                flag  = True
        if move == "down":
            x, y = player_position
            new_y = y + 100
            if (x, new_y) in adjacent_nodes:
                player_position  = (x, new_y)
                move = None
                flag = True
            
        if move == "left":
            x, y = player_position
            new_x = x - 100
            if (new_x, y) in adjacent_nodes:
                player_position = (new_x, y) 
                move = None
                flag = True 

        if move == "right":
            x, y = player_position
            new_x = x + 100
            if (new_x, y) in adjacent_nodes:
                player_position = (new_x, y) 
                move = None
                flag = True

    
        # Draw the current player position
        pos = player_position
        pygame.draw.circle(screen, (255, 255, 0), pos, 10)

        #checks if player has lost
        if player_position == chaser_position:
            game_state = "game_over"

    
        #obtain a path to player and update chaser_position
        if flag:
            path = getShortestPath(graph, chaser_position, player_position)
            if path == -1:
                game_state = "game_over"
            else:
                chaser_position = path[0][1]
                flag = False

        #draw chaser
        pygame.draw.circle(screen,(255,0,0),chaser_position,10)

        if player_position == winner_position:
            game_state = "winner"
            level += 1
            print(level)

        pygame.display.flip()
        
    elif game_state == "game_over":
        lose_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    elif game_state == "winner":
        if level <= max_level:
            player_position = level_positions[level][0]
            winner_position = level_positions[level][1]
            chaser_position = level_positions[level][2]
            flag = False
            move = None
            game_state = "game"
        elif level > max_level:
            win_screen()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_state = "start_menu"
            if keys[pygame.K_q]:
                pygame.quit()
                sys.exit()
   
