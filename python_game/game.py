import pygame, os


RECTWIDTH = 70
RECTHEIGHT = 80

BACKGROUND = pygame.image.load(os.path.join('game1', 'chest.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND, (1366,740))
FRAME = pygame.image.load(os.path.join('game1', 'frame.png'))
FRAME = pygame.transform.scale(FRAME,(140,80))
BUTTON_R = pygame.image.load(os.path.join('game1', 'button_R.png'))
BUTTON_R = pygame.transform.scale(BUTTON_R,(80,80))
BUTTON_L = pygame.image.load(os.path.join('game1', 'button_L.png'))
BUTTON_L = pygame.transform.scale(BUTTON_L,(80,80))
BUTTON_O = pygame.image.load(os.path.join('game1', 'button_O.png'))
BUTTON_O = pygame.transform.scale(BUTTON_O,(80,80))
LETTER_A = pygame.image.load(os.path.join('game1/letters', 'letter_A.png'))
LETTER_A = pygame.transform.scale(LETTER_A, (RECTWIDTH, RECTHEIGHT))
LETTER_B = pygame.image.load(os.path.join('game1/letters', 'letter_B.png'))
LETTER_B = pygame.transform.scale(LETTER_B, (RECTWIDTH, RECTHEIGHT))
LETTER_C = pygame.image.load(os.path.join('game1/letters', 'letter_C.png'))
LETTER_C = pygame.transform.scale(LETTER_C, (RECTWIDTH, RECTHEIGHT))
LETTER_D = pygame.image.load(os.path.join('game1/letters', 'letter_D.png'))
LETTER_D = pygame.transform.scale(LETTER_D, (RECTWIDTH, RECTHEIGHT))
LETTER_E = pygame.image.load(os.path.join('game1/letters', 'letter_E.png'))
LETTER_E = pygame.transform.scale(LETTER_E, (RECTWIDTH, RECTHEIGHT))
LETTER_F = pygame.image.load(os.path.join('game1/letters', 'letter_F.png'))
LETTER_F = pygame.transform.scale(LETTER_F, (RECTWIDTH, RECTHEIGHT))
LETTER_G = pygame.image.load(os.path.join('game1/letters', 'letter_G.png'))
LETTER_G = pygame.transform.scale(LETTER_G, (RECTWIDTH, RECTHEIGHT))
LETTER_H = pygame.image.load(os.path.join('game1/letters', 'letter_H.png'))
LETTER_H = pygame.transform.scale(LETTER_H, (RECTWIDTH, RECTHEIGHT))
LETTER_J = pygame.image.load(os.path.join('game1/letters', 'letter_J.png'))
LETTER_J = pygame.transform.scale(LETTER_J, (RECTWIDTH, RECTHEIGHT))
LETTER_K = pygame.image.load(os.path.join('game1/letters', 'letter_K.png'))
LETTER_K = pygame.transform.scale(LETTER_K, (RECTWIDTH, RECTHEIGHT))
LETTER_N = pygame.image.load(os.path.join('game1/letters', 'letter_N.png'))
LETTER_N = pygame.transform.scale(LETTER_N, (RECTWIDTH, RECTHEIGHT))
LETTER_O = pygame.image.load(os.path.join('game1/letters', 'letter_O.png'))
LETTER_O = pygame.transform.scale(LETTER_O, (RECTWIDTH, RECTHEIGHT))
LETTER_P = pygame.image.load(os.path.join('game1/letters', 'letter_P.png'))
LETTER_P = pygame.transform.scale(LETTER_P, (RECTWIDTH, RECTHEIGHT))
LETTER_R = pygame.image.load(os.path.join('game1/letters', 'letter_R.png'))
LETTER_R = pygame.transform.scale(LETTER_R, (RECTWIDTH, RECTHEIGHT))
LETTER_S = pygame.image.load(os.path.join('game1/letters', 'letter_S.png'))
LETTER_S = pygame.transform.scale(LETTER_S, (RECTWIDTH, RECTHEIGHT))
LETTER_X = pygame.image.load(os.path.join('game1/letters', 'letter_X.png'))
LETTER_X = pygame.transform.scale(LETTER_X, (RECTWIDTH, RECTHEIGHT))
LETTER_Z = pygame.image.load(os.path.join('game1/letters', 'letter_Z.png'))
LETTER_Z = pygame.transform.scale(LETTER_Z, (RECTWIDTH, RECTHEIGHT))

IMAGES = [LETTER_A, LETTER_B, LETTER_C, LETTER_D, LETTER_E, LETTER_F, LETTER_G, LETTER_H, LETTER_J, LETTER_K, LETTER_N, LETTER_O,
          LETTER_P, LETTER_R, LETTER_S, LETTER_X, LETTER_Z]

SCREENWIDTH = 1366
SCREENHEIGHT = 740
SIZESCREEN = (SCREENWIDTH, SCREENHEIGHT)