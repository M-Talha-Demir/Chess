import pygame
import os

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1200, 900))

# Background
background = pygame.image.load('tahta.jpg')

# Icon Caption felan
pygame.display.set_caption("Chess")
icon = pygame.image.load('tahta.jpg')
pygame.display.set_icon(icon)

# Set the size for the image
DEFAULT_IMAGE_SIZE = (80, 80)


# image of pieces
w_piyonImg = pygame.image.load('./image/white-piyon.png')
w_kaleImg = pygame.image.load('./image/white-kale.png')
w_atImg = pygame.image.load('./image/white-at.png')
w_filImg = pygame.image.load('./image/white-fil.png')
w_vezirImg = pygame.image.load('./image/white-vezir.png')
w_sahImg = pygame.image.load('./image/white-şah.png')

b_piyonImg  = pygame.image.load('./image/black-piyon.png')
b_kaleImg   = pygame.image.load('./image/black-kale.png')
b_atImg     = pygame.image.load('./image/black-at.png')
b_filImg    = pygame.image.load('./image/black-fil.png')
b_vezirImg  = pygame.image.load('./image/black-vezir.png')
b_sahImg    = pygame.image.load('./image/black-şah.png')

# Scale the image to your needed size
w_piyonImg  = pygame.transform.scale(w_piyonImg, DEFAULT_IMAGE_SIZE)
w_kaleImg   = pygame.transform.scale(w_kaleImg , DEFAULT_IMAGE_SIZE)
w_atImg     = pygame.transform.scale(w_atImg   , DEFAULT_IMAGE_SIZE)
w_filImg    = pygame.transform.scale(w_filImg  , DEFAULT_IMAGE_SIZE)
w_vezirImg  = pygame.transform.scale(w_vezirImg, DEFAULT_IMAGE_SIZE)
w_sahImg    = pygame.transform.scale(w_sahImg  , DEFAULT_IMAGE_SIZE)

b_piyonImg  = pygame.transform.scale(b_piyonImg, DEFAULT_IMAGE_SIZE)
b_kaleImg   = pygame.transform.scale(b_kaleImg , DEFAULT_IMAGE_SIZE)
b_atImg     = pygame.transform.scale(b_atImg   , DEFAULT_IMAGE_SIZE)
b_filImg    = pygame.transform.scale(b_filImg  , DEFAULT_IMAGE_SIZE)
b_vezirImg  = pygame.transform.scale(b_vezirImg, DEFAULT_IMAGE_SIZE)
b_sahImg    = pygame.transform.scale(b_sahImg  , DEFAULT_IMAGE_SIZE)

# starting positions(dictionary)

# yerleşim_beyaz = {"bp1": [0, 1], "bp2": [1, 1], "bp3": [2, 1], "bp4": [3, 1], "bp5": [4, 1], "bp6": [5, 1], "bp7": [6, 1], "bp8": [7, 1], "bk1": [0, 0], "ba1": [1, 0], "bf1": [2, 0], "bv": [3, 0], "bş": [4, 0], "bf2": [5, 0], "ba2": [6, 0], "bk2": [7, 0],
#                   "wp1": [0, 6], "wp2": [1, 6], "wp3": [2, 6], "wp4": [3, 6], "wp5": [4, 6], "wp6": [5, 6], "wp7": [6, 6], "wp8": [7, 6], "wk1": [0, 7], "wa1": [1, 7], "wf1": [2, 7], "wv": [3, 7], "wş": [4, 7], "wf2": [5, 7], "wa2": [6, 7], "wk2": [7, 7]}

yerleşim_siyah = {"wp1": [0, 1], "wp2": [1, 1], "wp3": [2, 1], "wp4": [3, 1], "wp5": [4, 1], "wp6": [5, 1], "wp7": [6, 1], "wp8": [7, 1], "wk1": [0, 0], "wa1": [1, 0], "wf1": [2, 0], "wv": [3, 0], "wş": [4, 0], "wf2": [5, 0], "wa2": [6, 0], "wk2": [7, 0],
                  "bp1": [0, 6], "bp2": [1, 6], "bp3": [2, 6], "bp4": [3, 6], "bp5": [4, 6], "bp6": [5, 6], "bp7": [6, 6], "bp8": [7, 6], "bk1": [0, 7], "ba1": [1, 7], "bf1": [2, 7], "bv": [3, 7], "bş": [4, 7], "bf2": [5, 7], "ba2": [6, 7], "bk2": [7, 7]}
# mydict = {'george': 16, 'amber': 19}
# print(list(mydict.keys())[list(mydict.values()).index(16)])  # Prints george
class tahta():
    def fill(self, order):
        for piece in list(order.keys()):
            # print(piece)
            if "b" in piece:
                if "p" in piece:
                    screen.blit(b_piyonImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "k" in piece:
                    screen.blit(b_kaleImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "a" in piece:
                    screen.blit(b_atImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "f" in piece:
                    screen.blit(b_filImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "v" in piece:
                    screen.blit(b_vezirImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "ş" in piece:
                    screen.blit(b_sahImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
            elif "w" in piece:
                if "p" in piece:
                    screen.blit(w_piyonImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "k" in piece:
                    screen.blit(w_kaleImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "a" in piece:
                    screen.blit(w_atImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "f" in piece:
                    screen.blit(w_filImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "v" in piece:
                    screen.blit(w_vezirImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))
                elif "ş" in piece:
                    screen.blit(w_sahImg, (order[piece][0] * 93.75 + 75, order[piece][1] * 93.75 + 75))

    def change(self,order, location, destination):
        try:
            a = list(order.keys())[list(order.values()).index(location)]
            print(a)
            order[a] = destination
            print(order)
            return order
        except:
            print(location, destination)


# Game Loop
running = True
tahta = tahta()
tahta.fill(yerleşim_siyah)
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    tahta.fill(yerleşim_siyah)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)[0]:
            print("down")
            print(pygame.mouse.get_pos())
            print(int((pygame.mouse.get_pos()[1] - 75) / 93.75))
            print(int((pygame.mouse.get_pos()[0] - 75) / 93.75))
            seçim = [int((pygame.mouse.get_pos()[0] - 75) / 93.75),int((pygame.mouse.get_pos()[1] - 75) / 93.75)]
            print(pygame.mouse.get_pressed(num_buttons=3))

        if event.type == pygame.MOUSEBUTTONUP:
            print("up")
            print(seçim , [int((pygame.mouse.get_pos()[1] - 75) / 93.75), int((pygame.mouse.get_pos()[0] - 75) / 93.75)])
            yerleşim_siyah = tahta.change(yerleşim_siyah, seçim , [int((pygame.mouse.get_pos()[0] - 75) / 93.75), int((pygame.mouse.get_pos()[1] - 75) / 93.75)] )
            tahta.fill(yerleşim_siyah)
        # if event.type == pygame.mouse.get_pressed:
        #     print("pressed")

    pygame.display.update()
