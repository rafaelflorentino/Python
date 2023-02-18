# Objetivo: Faça um programa que rode uma musica.
# Entrada: Sem entrada.
# Saida: Reproduzir Musica.
# Autor: Rafael Florentino.

#import pygame
from pygame import mixer

mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
mixer.event.wait()
input('Agora você escuta?')