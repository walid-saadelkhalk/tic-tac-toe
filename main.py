import pygame
import pygame_menu
from pygame.locals import *

pygame.init()
surface = pygame.display.set_mode((600, 600))
width, height = 600, 600

background_color = (111, 195, 240)

custom_font = "police/RubikBubbles-Regular.ttf"
menu_theme = pygame_menu.themes.THEME_DARK.copy()

markers = []
pos = []

winner = 0
game_over = False

def start_the_game():
    global markers, game_over
    markers = [[0] * 3 for _ in range(3)]  # Reset the game board
    game_over = False
    run_game()

def run_game():
    global markers, game_over
    clicked = False
    player = 1
    run = True
    while run:
        grille()
        draw_markers()
        victoire()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if not game_over and markers[cell_x // 200][cell_y // 200] == 0:
                    markers[cell_x // 200][cell_y // 200] = player
                    player *= -1

        pygame.display.update()

def grille():
    background_color = (192, 16, 1)
    grid = (0, 0, 0)
    surface.fill(background_color)
    for x in range(1, 3):
        pygame.draw.line(surface, grid, (0, 200 * x), (600, 200 * x), 10)
        pygame.draw.line(surface, grid, (200 * x, 0), (200 * x, 600), 10)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                toji_x = pygame.image.load("images/x.png")
                surface.blit(toji_x, (x_pos * 200 + 50, y_pos * 200 + 25))
            if y == -1:
                toji_o = pygame.image.load("images/o.png")
                surface.blit(toji_o, (x_pos * 200 + 25, y_pos * 200 + 25))
            y_pos += 1
        x_pos += 1



def victoire():
    global winner
    global game_over
    x_pos = 0
    
    for x in markers:
        # vérification des colonnes
        if sum(x) == 3:
            winner = 1
            game_over = True
            background_color = (0, 0, 0)
            surface.fill(background_color)
            toji_victoire_1 = pygame.image.load("images/toji_victoire_1.png")
            surface.blit(toji_victoire_1, (150, 10))
            titre_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 40)
            titre = titre_font.render("VICTOIRE DU JOUEUR 1", True, (192, 16, 1))
            surface.blit(titre, (60, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            return menu.mainloop(surface) 
                      
        
        if sum(x) == -3:
            winner = 2
            game_over = True
            background_color = (255, 255, 255)
            surface.fill(background_color)
            toji_victoire_2 = pygame.image.load("images/toji_victoire_2.png")
            surface.blit(toji_victoire_2, (40, 7))
            titre_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 40)
            titre = titre_font.render("VICTOIRE DU JOUEUR 2", True, (192, 16, 1))
            surface.blit(titre, (60, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            return menu.mainloop(surface)
            
            

        # vérification des lignes
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3:
            winner = 1
            game_over = True
            background_color = (0, 0, 0)
            surface.fill(background_color)
            toji_victoire_1 = pygame.image.load("images/toji_victoire_1.png")
            surface.blit(toji_victoire_1, (150, 10))
            titre_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 40)
            titre = titre_font.render("VICTOIRE DU JOUEUR 1", True, (192, 16, 1))
            surface.blit(titre, (60, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            return menu.mainloop(surface)
            
        
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3:
            winner = 2
            game_over = True
            background_color = (255, 255, 255)
            surface.fill(background_color)
            toji_victoire_2 = pygame.image.load("images/toji_victoire_2.png")
            surface.blit(toji_victoire_2, (40, 7))
            titre_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 40)
            titre = titre_font.render("VICTOIRE DU JOUEUR 2", True, (192, 16, 1))
            surface.blit(titre, (60, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            return menu.mainloop(surface)
        x_pos += 1

        # vérification des diagonales
        if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
            winner = 1
            game_over = True
            background_color = (0, 0, 0)
            surface.fill(background_color)
            toji_victoire_1 = pygame.image.load("images/toji_victoire_1.png")
            surface.blit(toji_victoire_1, (150, 10))
            titre_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 40)
            titre = titre_font.render("VICTOIRE DU JOUEUR 1", True, (192, 16, 1))
            surface.blit(titre, (60, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            return menu.mainloop(surface)        
            
        
        if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
            winner = 2
            game_over = True
            background_color = (255, 255, 255)
            surface.fill(background_color)
            toji_victoire_2 = pygame.image.load("images/toji_victoire_2.png")
            surface.blit(toji_victoire_2, (40, 7))
            titre_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 40)
            titre = titre_font.render("VICTOIRE DU JOUEUR 2", True, (192, 16, 1))
            surface.blit(titre, (60, 500))
            pygame.display.update()
            pygame.time.delay(3000)
            return menu.mainloop(surface)
            
        if game_over == False:
            tie = True
            for row in markers:
                for i in row:
                    if i == 0:
                        tie = False
            if tie == True:
                game_over = True
                background_color = (128, 128, 128)
                surface.fill(background_color)
                toji_egalite = pygame.image.load("images/toji_egalite.png")
                surface.blit(toji_egalite, (0, 60))
                message_font = pygame.font.Font("police/RubikBubbles-Regular.ttf", 50)
                message = message_font.render("Égalité !", True, (255, 255, 255))
                surface.blit(message, (200, 20))
                pygame.display.update()
                pygame.time.delay(3000)
                return menu.mainloop(surface)

        if game_over:
            pygame.time.delay(3000)  # Adjust this delay as needed
            start_the_game()  # Restart the game


# Titre
menu_theme.title_offset = (20, 40) 
menu_theme.title_font_color = (192, 16, 1)
menu_theme.title_font_size = 80 
menu_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE  

# Boutons
menu_theme.background_color = background_color  
menu_theme.title_font = custom_font
menu_theme.widget_font = custom_font
menu_theme.widget_font_size = 40 
menu_theme.widget_font_color = (0, 0, 0)
menu_theme.widget_position = (50, 50)
menu_theme.widget_padding = 20  
menu_theme.selection_color = (192, 16, 1)
menu_theme.selection_border_width = 0


# Menu général
menu = pygame_menu.Menu('TIC TAC TOJI', 600, 600, theme=menu_theme)

# Ajouter une image au menu
image_path = "images/sabre.png"
menu.add.image(image_path, scale=(1, 1), angle=0)


# Ajouter un bouton au menu
menu.add.button('JOUER', start_the_game)
menu.add.button('QUITTER', pygame_menu.events.EXIT)


menu.mainloop(surface)


pygame.quit()