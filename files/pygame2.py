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


    def set_view_live(self, left11, top11, x_11, y_11):
        self.left11 = left11
        self.top11 = top11
        self.x_11 = x_11
        self.y_11 = y_11


    def set_view_prot(self, left12, top12, x_12, y_12):
        self.left12 = left12
        self.top12 = top12
        self.x_12 = x_12
        self.y_12 = y_12


    def set_view_power(self, left13, top13, x_13, y_13):
        self.left13 = left13
        self.top13 = top13
        self.x_13 = x_13
        self.y_13 = y_13


    def set_view_crit(self, left14, top14, x_14, y_14):
        self.left14 = left14
        self.top14 = top14
        self.x_14 = x_14
        self.y_14 = y_14


    def set_view_out(self, left0, top0, x_0, y_0):
        self.left0 = left0
        self.top0 = top0
        self.x_0 = x_0
        self.y_0 = y_0


##    def set_view4(self, left4, top4, x_4, y_4):
##        self.left4 = left4
##        self.top4 = top4
##        self.x_4 = x_4
##        self.y_4 = y_4
        

    def render(self, surface):
        wcolor = pygame.Color("white")
        if flag == 0:
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
        elif flag == 1:
            for i in range(self.height):
                for j in range(self.width):
                    pygame.draw.rect(surface, wcolor,
                                     (self.left11 + self.x_11 * j, self.top11 + self.y_11 * i,
                                      self.x_11, self.y_11),
                                     1 if self.board[i][j] == 0 else 0)
            for i in range(self.height):
                for j in range(self.width):
                    pygame.draw.rect(surface, wcolor,
                                     (self.left12 + self.x_12 * j, self.top12 + self.y_12 * i,
                                      self.x_12, self.y_12),
                                     1 if self.board[i][j] == 0 else 0)
            for i in range(self.height):
                for j in range(self.width):
                    pygame.draw.rect(surface, wcolor,
                                     (self.left13 + self.x_13 * j, self.top13 + self.y_13 * i,
                                      self.x_13, self.y_13),
                                     1 if self.board[i][j] == 0 else 0)
            for i in range(self.height):
                for j in range(self.width):
                    pygame.draw.rect(surface, wcolor,
                                     (self.left14 + self.x_14 * j, self.top14 + self.y_14 * i,
                                      self.x_14, self.y_14),
                                     1 if self.board[i][j] == 0 else 0)
            for i in range(self.height):
                for j in range(self.width):
                    pygame.draw.rect(surface, wcolor,
                                     (self.left0 + self.x_0 * j, self.top0 + self.y_0 * i,
                                      self.x_0, self.y_0),
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
        if flag == 0:
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
        elif flag == 1:
            if cell_coords[0] > self.left11 and cell_coords[0] < self.x_11 + self.left11:
                if cell_coords[1] > self.top11 and cell_coords[1] < self.y_11 + self.top11:
                    print("кнопкаlive")
            if cell_coords[0] > self.left12 and cell_coords[0] < self.x_12 + self.left12:
                if cell_coords[1] > self.top12 and cell_coords[1] < self.y_12 + self.top12:
                    print("кнопкаprot")
            if cell_coords[0] > self.left13 and cell_coords[0] < self.x_13 + self.left13:
                if cell_coords[1] > self.top13 and cell_coords[1] < self.y_13 + self.top13:
                    print("кнопкаpower")
            if cell_coords[0] > self.left14 and cell_coords[0] < self.x_14 + self.left14:
                if cell_coords[1] > self.top14 and cell_coords[1] < self.y_14 + self.top14:
                    print("кнопкаcrit")
            if cell_coords[0] > self.left0 and cell_coords[0] < self.x_0 + self.left0:
                if cell_coords[1] > self.top0 and cell_coords[1] < self.y_0 + self.top0:
                    print("кнопкаout")
                    flag = 0
    
            
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

        board.set_view_live(200, 200, 200, 300)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        board.set_view_prot(450, 200, 200, 300)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        board.set_view_power(700, 200, 200, 300)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        board.set_view_crit(950, 200, 200, 300)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        board.set_view_out(1315, 10, 25, 25)
        text = font.render("Магазин", True, (100, 255, 100))
        screen.blit(text, (595, 420))
        
        #board.set_view4(425, 300, 500, 75)
    for event in pygame.event.get():
        f2 = flag
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(event.pos)
##        if event.type == pygame.MOUSEMOTION:
##            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
##        screen.fill((0, 0, 0))
        if f2 == flag:
            board.render(screen)
            pygame.display.flip()
            clock.tick(fps)
        else:
            break
pygame.quit()
