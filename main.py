import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game Screen")
screen.fill((58,58,58))
#bg = pygame.image.load(pygame.Color(58,58,58)).convert()
#bg_image = pygame.transform.scale(bg,(400,500))

fg = pygame.image.load("smiley.jpeg").convert()
fg_image = pygame.transform.scale(fg,(300,300))

txt = pygame.font.Font(None, 40).render("Keep smiling",True,pygame.Color("yellow"))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #screen.blit(bg_image,(0,0))
    screen.blit(fg_image,(100,120))
    screen.blit(txt,(160,90))
    pygame.display.flip()
pygame.quit()
   

