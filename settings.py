import pygame, os, sys

pygame.mixer.init()

WIDTH = 1500
HEIGHT = 800
WINDOW = (WIDTH, HEIGHT)
FPS = 60

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

for i in range(1,10):
	PLAYER_SPRTIES_LT.append(load_img(
		os.path.join(IMG_PATH, str(i) + ".png"),
		 (PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT)
	))

VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "kaczynski.png")), (60,60)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "don_kasjo.png")), (90,90)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "saleta.png")), (90,90)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "stanowski.png")), (90,140)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "ostaszewska.png")), (90,100)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "lempart.png")), (100,100)))
VILLAIN_LT.append(load_img((os.path.join(IMG_PATH, "binkowski.png")), (120,100)))


BULLET_IMG = load_img(os.path.join(IMG_PATH, "mandarynka.png"), (25,21))
PUNCH_SND = pygame.mixer.Sound(os.path.join(SND_PATH, "uderzenie.wav")) 
FAKEN = pygame.mixer.Sound(os.path.join(SND_PATH, "faken.wav"))

GAME_TITLE = "The Oftenhide Defence"

