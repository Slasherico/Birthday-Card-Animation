import pygame, time
pygame.init()

display_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Birthday Greeting Card')

img1 = pygame.image.load('images/Blank_Paper.jpg')
img2 = pygame.image.load('images/Cake.jpg')
img3 = pygame.image.load('images/Present.jpg')

imge1 = pygame.transform.scale(img1, (600, 600))
imge2 = pygame.transform.scale(img2, (600, 600))
imge3 = pygame.transform.scale(img3, (600, 600))

font = pygame.font.SysFont('Aptos', 72)
h_text = font.render('Happy', True, 'Red')
b_text = font.render('Birthday', True, 'Blue')

images = [imge1, imge2, imge3]
index = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    display_surface.fill('White')
    
    display_surface.blit(images[index], (0, 0))
    
    display_surface.blit(h_text, (200, 200))
    display_surface.blit(b_text, (400, 200))
    
    pygame.display.update()
    
    time.sleep(2)
    
    index = (index + 1) % len(images)
    clock.tick(30)

pygame.quit()