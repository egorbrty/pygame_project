import pygame


flag = 0

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.x_1 = 30
        self.y_1 = 30

 
    def set_view1(self, left1, top1, x_1, y_1):
        self.left1 = left1
        self.top1 = top1
        self.x_1 = x_1
        self.y_1 = y_1


    def set_view2(self, left2, top2, x_2, y_2):
        self.left2 = left2
        self.top2 = top2
        self.x_2 = x_2
        self.y_2 = y_2


    def set_view3(self, left3, top3, x_3, y_3):
        self.left3 = left3
        self.top3 = top3
        self.x_3 = x_3
        self.y_3 = y_3


##    def set_view4(self, left4, top4, x_4, y_4):
##        self.left4 = left4
##        self.top4 = top4
##        self.x_4 = x_4
##        self.y_4 = y_4
        

    def render(self, surface):
        wcolor = pygame.Color("white")
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, wcolor,
                                 (self.left1 + self.x_1 * j, self.top1 + self.y_1 * i,
                                  self.x_1, self.y_1),
                                 1 if self.board[i][j] == 0 else 0)
        wcolor = pygame.Color("white")
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, wcolor,
                                 (self.left2 + self.x_2 * j, self.top2 + self.y_2 * i,
                                  self.x_2, self.y_2),
                                 1 if self.board[i][j] == 0 else 0)
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, wcolor,
                                 (self.left3 + self.x_3 * j, self.top3 + self.y_3 * i,
                                  self.x_3, self.y_3),
                                 1 if self.board[i][j] == 0 else 0)
##        for i in range(self.height):
##            for j in range(self.width):
##                pygame.draw.rect(surface, wcolor,
##                                 (self.left4 + self.x_4 * j, self.top4 + self.y_4 * i,
##                                  self.x_4, self.y_4),
##                                 1 if self.board[i][j] == 0 else 0)

 
    def get_click(self, mouse_pos):
        cell_coords = self.get_cell(mouse_pos)
        if cell_coords is None:
            return
 
        self.on_click(cell_coords)
        
 
    def get_cell(self, mouse_pos):
        board_width = self.width * self.x_1
        board_height = self.height * self.y_1
        if self.left1 < mouse_pos[0] < self.left1 + board_width:
            if self.top1 < mouse_pos[1] < self.top1 + board_height:
                cell_coords = (mouse_pos[1] - self.left1) // self.x_1,
                (mouse_pos[0] - self.top1) // self.y_1
                return cell_coords
        return None
    
 
    def on_click(self, cell_coords):
        global flag
        #print(cell_coords)
##        if cell_coords[0] > self.left4 and cell_coords[0] < self.x_4 + self.left4:
##            if cell_coords[1] > self.top4 and cell_coords[1] < self.y_4 + self.top4:
##                print("кнопка1")
        if cell_coords[0] > self.left3 and cell_coords[0] < self.x_3 + self.left3:
            if cell_coords[1] > self.top3 and cell_coords[1] < self.y_3 + self.top3:
                print("кнопка1")
                flag = 1
        if cell_coords[0] > self.left2 and cell_coords[0] < self.x_2 + self.left2:
            if cell_coords[1] > self.top2 and cell_coords[1] < self.y_2 + self.top2:
                print("кнопка2")
        if cell_coords[0] > self.left1 and cell_coords[0] < self.x_1 + self.left1:
            if cell_coords[1] > self.top1 and cell_coords[1] < self.y_1 + self.top1:
                print("кнопка3")
    
            
pygame.init()
fps = 20
clock = pygame.time.Clock()
size = 1350, 700
screen = pygame.display.set_mode(size)
##board = Board(1, 1)
##board.set_view1(100, 400, 300, 50)
##board.set_view2(100, 300, 300, 50)
##board.set_view3(100, 200, 300, 50)
##board.set_view4(100, 100, 300, 50)
running = True
while running:
    if flag == 0:   
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        board = Board(1, 1)

        board.set_view3(425, 400, 500, 75)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        board.set_view2(425, 500, 500, 75)
        text = font.render("Выбрать уровень", True, (100, 255, 100))
        screen.blit(text, (540, 520))
        board.set_view1(425, 600, 500, 75)
        text = font.render("Продолжить историю", True, (100, 255, 100))
        screen.blit(text, (490, 620))
        #board.set_view4(425, 300, 500, 75)
    elif flag == 1:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        board = Board(1, 1)

        board.set_view3(425, 400, 500, 75)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        board.set_view2(425, 500, 500, 75)
        text = font.render("Выбвень", True, (100, 255, 100))
        screen.blit(text, (540, 520))
        board.set_view1(425, 600, 500, 75)
        text = font.render("Продоорию", True, (100, 255, 100))
        screen.blit(text, (490, 620))
        #board.set_view4(425, 300, 500, 75)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
##        if event.type == pygame.MOUSEMOTION:
##            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
##        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
pygame.quit()
