import pygame, sys, asyncio
from pygame.locals import QUIT

async def main():
#def main():
    pygame.init()
    global window
    window = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Stormwater Distribution Simulator')
    window.fill("lightblue")

    maxFPS = 60
    clock = pygame.time.Clock()

    city = pygame.image.load("city_fitted.png")
    window.blit(city, (-1, -1))

    def drawButton(screen, button, border, buttonR, buttonText):
        pygame.draw.rect(screen, button, buttonR, border_radius=2)
        pygame.draw.rect(screen, border, buttonR, border_radius=2, width=2)
        screen.blit(buttonText, (buttonR.x + buttonR.width/2 - buttonText.get_width()/2,
                                buttonR.y + buttonR.height/2 - buttonText.get_height()/2,))
    
    def conditionButton(screen, button, border, buttonC, buttonText):
        pygame.draw.rect(screen, button, buttonC, border_radius=2)
        pygame.draw.rect(screen, border, buttonC, border_radius=2, width=2)
        screen.blit(buttonText, (buttonC.x + buttonC.width/2 - buttonText.get_width()/2,
                                buttonC.y + buttonC.height/2 - buttonText.get_height()/2,))

    fontType = pygame.font.SysFont("arial", 16, True, False)
    conditionalFont = pygame.font.SysFont("arial", 12, True, False)
    global water
    water = False
    # colored area
    pygame.draw.rect(window, "darkgray", pygame.Rect(1000, 0, 200, 800))
    global waterButton, restartButton, endButton

    # water button
    if not water:
        waterText = fontType.render("Add Water", True, "black")
    else:
        waterText = fontType.render("Remove Water", True, "black")
    waterButton = pygame.Rect(1050, 200, 100, 50)
    drawButton(window, "silver", "black", waterButton, waterText)

    # reset button
    restartText = fontType.render("Reset", True, "black")
    restartButton = pygame.Rect(1050, 300, 100, 50)
    drawButton(window, "silver", "black", restartButton, restartText)

    # end button
    endText = fontType.render("End", True, "black")
    endButton = pygame.Rect(1050, 400, 100, 50)
    drawButton(window, "silver", "black", endButton, endText)

    # write what each number on the condition buttons mean
    window.blit(conditionalFont.render("1 - Create a stormwater sewer system", True, "black"), (1005, 575))
    window.blit(conditionalFont.render("2 - Add green roofs to buildings", True, "black"), (1005, 600))
    window.blit(conditionalFont.render("3 - Water-permeable pavement", True, "black"), (1005, 625))

    """
    Create variables for each change the player can make as boolean values
    - increase drainwater pipe sizes, make a separate stormwater sewer
    - change the pavement to be permeable
    - add green roofs
    """
    add_condition = True

    stormwater_sewer = False
    Csewer = "silver"
    sewerText = fontType.render("1", True, "black")
    sewerButton = pygame.Rect(500, 600, 40, 40)

    permeable = False
    Cperm = "silver"
    permText = fontType.render("3", True, "black")
    permButton = pygame.Rect(400, 200, 40, 40)

    green_roofs = False
    Cgreen = "silver"
    greenText = fontType.render("2", True, "black")
    greenButton = pygame.Rect(200, 400, 40, 40)

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
                if sewerButton.collidepoint(event.pos):
                    sewerButton = pygame.Rect(500, 600, 50, 50)
                    drawButton(window, "lightgray", "black", sewerButton, sewerText)
                else:
                    sewerButton = pygame.Rect(500, 600, 40, 40)
                    drawButton(window, "lightgray", "black", sewerButton, sewerText)
                if greenButton.collidepoint(event.pos):
                    greenButton = pygame.Rect(200, 400, 50, 50)
                    drawButton(window, "lightgray", "black", greenButton, greenText)
                else:
                    greenButton = pygame.Rect(200, 400, 40, 40)
                    drawButton(window, "lightgray", "black", greenButton, greenText)
                if permButton.collidepoint(event.pos):
                    permButton = pygame.Rect(400, 200, 50, 50)
                    drawButton(window, "lightgray", "black", permButton, permText)
                else:
                    permButton = pygame.Rect(400, 200, 40, 40)
                    drawButton(window, "lightgray", "black", permButton, permText)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
            # ----------------------------------------------------------------------------------------------- #
                if waterButton.collidepoint(event.pos):
                    drawButton(window, "gray95", "black", waterButton, waterText)
                    if water:
                        water = False
                        city = pygame.image.load("city_fitted.png")
                    else:
                        water = True
                    
                    if water:
                        if not stormwater_sewer and not permeable and not green_roofs:
                            city = pygame.image.load("flooded.jpg")
                        elif stormwater_sewer and not permeable and not green_roofs:
                            city = pygame.image.load("stormwater_drain.jpg")
                        elif not stormwater_sewer and permeable and not green_roofs:
                            city = pygame.image.load("permeable_walkways.jpg")
                        elif not stormwater_sewer and not permeable and  green_roofs:
                            city = pygame.image.load("green_roofed_water.jpg")
                    city = pygame.transform.scale(city, (1000, 800))

                else:
                    drawButton(window, "silver", "black", waterButton, waterText)
            # ----------------------------------------------------------------------------------------------- #
                if restartButton.collidepoint(event.pos):
                    drawButton(window, "gray95", "black", restartButton, restartText)
                    city = pygame.image.load("city_fitted.png")
                    add_condition = True
                    stormwater_sewer = False
                    permeable = False
                    green_roofs = False
                    water = False
                    Csewer = "silver"
                    Cgreen = "silver"
                    Cperm = "silver"
                else:
                    drawButton(window, "silver", "black", restartButton, restartText)
                if endButton.collidepoint(event.pos):
                    drawButton(window, "gray95", "black", endButton, endText)
                    pygame.quit()
                    sys.exit()
                else:
                    drawButton(window, "silver", "black", endButton, endText)
                if sewerButton.collidepoint(event.pos) and add_condition:
                    stormwater_sewer = True
                    add_condition = False
                    Csewer = "gray95"
                if greenButton.collidepoint(event.pos) and add_condition:
                    green_roofs = True
                    add_condition = False
                    Cgreen = "gray95"
                if permButton.collidepoint(event.pos) and add_condition:
                    permeable = True
                    add_condition = False
                    Cperm = "gray95"
        
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
        drawButton(window, Csewer, "black", sewerButton, sewerText)
        drawButton(window, Cgreen, "black", greenButton, greenText)
        drawButton(window, Cperm, "black", permButton, permText)
        
        pygame.display.update()
        await asyncio.sleep(0)


# if __name__ == "__main__":
#     main()

asyncio.run(main())
