# Prueba salida audio RaspBerry Pi 3 model B+

import sounddevice as sd
import numpy as np
from pydub import AudioSegment

# Cargar el archivo de audio .wav
archivo_audio = "./Wav/CHH05 Drums1DOTcom.wav"  # Reemplaza con el nombre de tu archivo

# Cargar el archivo de audio usando pydub
audio = AudioSegment.from_wav(archivo_audio)

# Convertir el audio a un array numpy (esto es necesario para usar sounddevice)
audio_np = np.array(audio.get_array_of_samples())

# Obtener la frecuencia de muestreo del archivo
frecuencia_muestreo = audio.frame_rate

while True:
    # Reproducir el audio a través del conector de 3.5 mm
    print("Reproduciendo audio por el conector de 3.5 mm...")
    sd.play(audio_np, samplerate=frecuencia_muestreo)
    sd.wait()  # Esperar hasta que termine la reproducción
    print("Reproducción terminada.")
