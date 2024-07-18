import pygame, sys
from pygame.locals import QUIT

def main():
    test = pygame.image.load("city_flooded.jpg")
    print(test.get_size())
    pygame.init()
    global window
    window = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Stormwater Distribution Simulator')
    window.fill("lightblue")

    maxFPS = 60
    clock = pygame.time.Clock()

    city = pygame.image.load("city_fitted.png")
    window.blit(city, (-1, -1))

    """
    draw on the right hand side a control panel with the buttons:
    - Add/Remove Water
    - Reset
    - End
    """
    fontType = pygame.font.SysFont("arial", 16, True, False)
    global water
    water = False
    #colored area
    pygame.draw.rect(window, "darkgray", pygame.Rect(1000, 0, 200, 800))
    global waterButton, restartButton, endButton

    #water button
    if not water:
        waterText = fontType.render("Add Water", True, "black")
    else:
        waterText = fontType.render("Remove Water", True, "black")
    waterButton = pygame.Rect(1050, 200, 100, 50)
    drawButton(window, "silver", "black", waterButton, waterText)

    #reset button
    restartText = fontType.render("Reset", True, "black")
    restartButton = pygame.Rect(1050, 375, 100, 50)
    drawButton(window, "silver", "black", restartButton, restartText)

    #end button
    endText = fontType.render("End", True, "black")
    endButton = pygame.Rect(1050, 550, 100, 50)
    drawButton(window, "silver", "black", endButton, endText)

    """
    Create variables for each change the player can make as boolean values
    """
    # global anything_to_help
    # anything_to_help = False


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION:
                if waterButton.collidepoint(event.pos):
                    drawButton(window, "lightgray", "black", waterButton, waterText)
                else:
                    drawButton(window, "silver", "black", waterButton, waterText)
                if restartButton.collidepoint(event.pos):
                    drawButton(window, "lightgray", "black", restartButton, restartText)
                else:
                    drawButton(window, "silver", "black", restartButton, restartText)
                if endButton.collidepoint(event.pos):
                    drawButton(window, "lightgray", "black", endButton, endText)
                else:
                    drawButton(window, "silver", "black", endButton, endText)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if waterButton.collidepoint(event.pos):
                    drawButton(window, "gray95", "black", waterButton, waterText)
                    if water:
                        water = False
                        city = pygame.image.load("city_fitted.png")
                    else:
                        water = True
                        city = pygame.image.load("city_flooded.jpg")
                        city = pygame.transform.scale(city, (1000, 800))
                else:
                    drawButton(window, "silver", "black", waterButton, waterText)
                if restartButton.collidepoint(event.pos):
                    drawButton(window, "gray95", "black", restartButton, restartText)
                else:
                    drawButton(window, "silver", "black", restartButton, restartText)
                if endButton.collidepoint(event.pos):
                    drawButton(window, "gray95", "black", endButton, endText)
                else:
                    drawButton(window, "silver", "black", endButton, endText)
        
            if event.type == pygame.MOUSEBUTTONUP:
                if waterButton.collidepoint(event.pos):
                    drawButton(window, "lightgray", "black", waterButton, waterText)
                else:
                    drawButton(window, "silver", "black", waterButton, waterText)
                if restartButton.collidepoint(event.pos):
                    drawButton(window, "lightgray", "black", restartButton, restartText)
                else:
                    drawButton(window, "silver", "black", restartButton, restartText)
                if endButton.collidepoint(event.pos):
                    drawButton(window, "lightgray", "black", endButton, endText)
                else:
                    drawButton(window, "silver", "black", endButton, endText)
        
        if not water:
            waterText = fontType.render("Add Water", True, "black")
        else:
            waterText = fontType.render("Dry", True, "black")

        window.blit(city, (-1, -1))
        pygame.display.update()


def drawButton(screen, button, border, buttonR, buttonText):
    pygame.draw.rect(screen, button, buttonR, border_radius=2)
    pygame.draw.rect(screen, border, buttonR, border_radius=2, width=2)
    screen.blit(buttonText, (buttonR.x + buttonR.width/2 - buttonText.get_width()/2,
                             buttonR.y + buttonR.height/2 - buttonText.get_height()/2,))


if __name__ == "__main__":
    main()
