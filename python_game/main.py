import pygame, os
import game as gm
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('BubbleSort Lockpick Master')
clock = pygame.time.Clock()

screen.blit(gm.BACKGROUND, (0, 0))

class Letter(pygame.sprite.Sprite):
    def __init__(self, x,y, file_image, value):
        super().__init__()
        self._image = file_image
        self._lvalue = value
        self.rect = self.image.get_rect()
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def image(self):
        return self._image

    @property
    def lvalue(self):
        return self._lvalue

    @x.setter
    def x(self, value):
        self._x = value

    @image.setter
    def image(self, value):
        self._image = value

    @lvalue.setter
    def lvalue(self, value):
        self._lvalue = value

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


random_numbers = random.sample(range(17),10)
random_board = []
random_board_copy = []
random_board_sort = []
x_ofs = 385
y_ofs = 128
for number in random_numbers:
    random_board.append(Letter(x_ofs, y_ofs, gm.IMAGES[number], number))
    random_board_copy.append(Letter(x_ofs, y_ofs, gm.IMAGES[number], number))
    random_board_sort.append(Letter(x_ofs, y_ofs, gm.IMAGES[number], number))
    x_ofs = x_ofs + gm.RECTWIDTH + 1


class Frame(pygame.sprite.Sprite):
    index_left = 0
    index_right = 1
    step = 0
    play_again = 0
    end = 0

    def __init__(self, x,y, file_image, sort_steps):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.movement_x = 0
        self.x = x
        self.y = y
        self.sort_steps = sort_steps


    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move_right(self):
        if self.x > 882:
            self.x  = 385
            self.index_left = 0
            self.index_right = 1
        else:
            self.x = self.x + 71
            self.index_left = self.index_left + 1
            self.index_right = self.index_right + 1
            #print(self.index_left)
            #print(self.index_right)

    def move_left(self):
        if self.x < 456:
            self.x = 953
            self.index_left = 8
            self.index_right = 9
        else:
            self.x = self.x - 71
            self.index_left = self.index_left - 1
            self.index_right = self.index_right - 1
            #print(self.index_left)
            #print(self.index_right)

    def stop(self):
        self.movement_x = 0

    def update(self):
        self.x += self.movement_x

    def swap_letterz(self, board, board_copy):
            if self.sort_steps.step[self.step][0] == self.index_left:
                board[self.index_left].x, board[self.index_right].x = board[self.index_right].x, board[self.index_left].x
                board[self.index_left], board[self.index_right] = board[self.index_right], board[self.index_left]

                #for i in board:
                    #print(i.lvalue, i.x)
                self.step += 1
                #print(self.index_left, self.index_right)
                if self.step == self.sort_steps.steps:
                    print("Gratulacje! Zwycięstwo!")
                    self.end = 1
            else:
                print("Przegrałeś! Spróbuj jeszcze raz.")
                self.step = 0
                self.play_again = 1
                i = 0
                while i < len(board):
                    #print(board[i].lvalue)
                    #print(board_copy[i].lvalue)
                    board[i].x = board_copy[i].x
                    board[i].lvalue = board_copy[i].lvalue
                    board[i].image = board_copy[i].image
                    i += 1

class BubbleSort:
    steps = 0
    step = []

    def __init__(self, board):
        self.board_to_sort = board

    def sort_step(self):
        n = len(self.board_to_sort)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.board_to_sort[j].lvalue > self.board_to_sort[j+1].lvalue:
                    self.board_to_sort[j], self.board_to_sort[j+1] = self.board_to_sort[j+1], self.board_to_sort[j]
                    self.step.append([j, j+1])
                    self.steps += 1
        #print(self.step)
        #print(self.steps)

bubbleSort = BubbleSort(random_board_sort[:])
bubbleSort.sort_step()

frame = Frame(385, 128, gm.FRAME, bubbleSort)


class Button(pygame.sprite.Sprite):
    def __init__(self, x,y, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                #print("clicked")
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            return False

buttonL = Button(385,230,gm.BUTTON_L)
buttonR = Button(485, 230, gm.BUTTON_R)
buttonO = Button(985, 230, gm.BUTTON_O)


window_open = True
while window_open:
    for letter in random_board:
        letter.draw(screen)
    frame.draw(screen)
    buttonL.draw(screen)
    buttonR.draw(screen)
    buttonO.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        if buttonL.get_event(event) == True:
           frame.move_left()
        elif buttonR.get_event(event) == True:
            frame.move_right()
        elif buttonO.get_event(event) == True:
            frame.swap_letterz(random_board, random_board_copy[:])
        else:
            frame.stop()


    pygame.display.flip()
    clock.tick(30)
    if frame.end == 1:
        window_open = False
pygame.quit()