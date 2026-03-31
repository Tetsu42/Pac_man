import pygame
# import sys
import asyncio

#initialiser tous les modules
pygame.init()

async def main():
    window_width = 800
    window_height = 600
    clock = pygame.time.Clock()

    #Affichage de l'écran
    window = pygame.display.set_mode((window_width, window_height))

    game = True

    #boucle pour que la fenetre reste active
    while game:

        #ecoute des evenements
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game = False

        #peint le background en noir
        window.fill((0, 0, 0))

        #MAJ de tous les contenus graphiques
        pygame.display.flip()
        clock.tick(60)

        # Necessaire pour laisser la main a la boucle asyncio (web/pygbag)
        await asyncio.sleep(0)

asyncio.run(main())