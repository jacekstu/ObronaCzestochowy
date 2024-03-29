import pygame, os, sys

pygame.mixer.init()

GRAVITY_LT = [0.2, 0.1]

WIDTH = 1500
HEIGHT = 800
WINDOW = (WIDTH, HEIGHT)
FPS = 60
screen = pygame.display.set_mode(WINDOW)

# COLORS
BLACK = (0,0,0)

SPAWNNING_TIMER = 3

def load_img(path, res):
	img = pygame.image.load(path)
	img = pygame.transform.scale(img, res)
	return img

def terminate_game():
	pygame.quit()
	sys.exit()

IMG_PATH = os.path.join(os.environ.get('HOME'), "assets/imgs")
SND_PATH = os.path.join(os.environ.get('HOME'), "assets/snds")

PLAYER_SPRITE_HEIGHT = 150
PLAYER_SPRITE_WIDTH = 90
PLAYER_SPRTIES_LT = []
VILLAIN_LT = []
SPLASHING_FRUIT_LT = []
SPLASHING_FRUIT_LT2 = []

for i in range(1,10):
	PLAYER_SPRTIES_LT.append(load_img(
		os.path.join(IMG_PATH, str(i) + ".png"),
		 (PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT)
	))

# Load splashing fruit images
for i in range(1,8):
	SPLASHING_FRUIT_LT.append(load_img(
		os.path.join(IMG_PATH, "m" + str(i) + ".png"),
		(35,30)
	))

# Load splashing fruit images
for i in range(1,8):
	SPLASHING_FRUIT_LT2.append(load_img(
		os.path.join(IMG_PATH, "s" + str(i) + ".png"),
		(65,61)
	))


BOTTOM_LINE_FOR_ORANGES = HEIGHT - 55


VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "kaczynski.png")), (60,60)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "don_kasjo.png")), (90,90)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "saleta.png")), (90,90)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "stanowski.png")), (90,140)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "ostaszewska.png")), (90,100)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "lempart.png")), (100,100)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "binkowski.png")), (120,100)))


BULLET_IMG = load_img(os.path.join(IMG_PATH, "mandarynka.png"), (20,20))
#BULLET_IMG = load_img(os.path.join(IMG_PATH, "test.png"), (25,21))
PUNCH_SND = pygame.mixer.Sound(os.path.join(SND_PATH, "uderzenie.wav")) 
FAKEN = pygame.mixer.Sound(os.path.join(SND_PATH, "faken.wav"))

SMASHED_ORANGE = load_img(os.path.join(IMG_PATH, 'm5.png'), (33,28))
GAME_TITLE = "The Oftenhide Defence"
HEALTHBAR_IMG = load_img(os.path.join(IMG_PATH, "healthbar_icon.png"), (60,60))
ROCKET_IMG = load_img(os.path.join(IMG_PATH, "piorun.png"), (30,50))
