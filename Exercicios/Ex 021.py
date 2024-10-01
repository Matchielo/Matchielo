# Programa para rodar uma simples musica

import pygame

# Inicializa o mixer e o pygame
pygame.init()
pygame.mixer.init()

# Corrige o caminho do arquivo MP3
pygame.mixer.music.load("C:/Users/mateus.lima/Desktop/Estudos Python/Exercicios/volare.mp3")

# Toca a música
pygame.mixer.music.play()
 
# Aguarda a entrada do usuário para manter o programa em execução
input("Pressione Enter para parar...")

# Mantém o evento do pygame ativo
pygame.event.wait()
