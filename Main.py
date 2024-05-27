import pygame
from car import Car
from kan_network import kAN

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    car1 = Car((255, 0, 0), kAN(2, 10, 2), [100, 500])
    car2 = Car((0, 0, 255), kAN(2, 10, 2), [100, 550])
    path = Path()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        path.draw(screen)
        car1.update(path)
        car2.update(path)

        car1.draw(screen)
        car2.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_simulation()
  
