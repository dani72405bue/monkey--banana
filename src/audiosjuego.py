import pygame
from setings import RUTA_SONIDO_MONO, RUTA_SONIDO_BANANA, RUTA_SONIDO_PERDIO


class AudioJuego:
	def __init__(self):
		if not pygame.mixer.get_init():
			pygame.mixer.init()
		self.sonido_mono = pygame.mixer.Sound(RUTA_SONIDO_MONO)
		self.sonido_banana = pygame.mixer.Sound(RUTA_SONIDO_BANANA)
		self.sonido_perdio = pygame.mixer.Sound(RUTA_SONIDO_PERDIO)

	def reproducir_mono(self):
		self.sonido_mono.play()

	def reproducir_banana_aparece(self):
		self.sonido_banana.play()

	def reproducir_banana_coja(self):
		self.sonido_banana.play()

	def reproducir_perdio(self):
		self.sonido_perdio.play()
