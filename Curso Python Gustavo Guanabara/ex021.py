# DESAFIO 21
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.quit()
