# Prueba salida audio RaspBerry Pi 3 model B+

import pygame

# Inicializar el mezclador de audio de Pygame
pygame.mixer.init()

# Cargar el archivo de audio .wav
archivo_audio = "./Proyecto Final/Wav/CHH05 Drums1DOTcom.wav"  # Cambia esto al nombre de tu archivo de audio

# Cargar el sonido en el mezclador
pygame.mixer.music.load(archivo_audio)

# Reproducir el sonido
print("Reproduciendo audio en Windows...")
pygame.mixer.music.play()

# Mantener el script en ejecución hasta que termine el audio
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Control de tiempo para esperar la finalización

print("Reproducción terminada.")
