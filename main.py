import os
import random

# Ruta a la carpeta con tus wallpapers
wallpaper_folder = '/home/ricardo/Imágenes/wallpapers'
# Lista de imágenes soportadas
image_extensions = ['.jpg', '.png', '.jpeg', '.webp']

# Duración en segundos de cada fondo y transición
static_duration = 1795.0  # Duración de cada imagen estática
transition_duration = 5.0  # Duración de cada transición

# Obtener todas las imágenes en la carpeta
wallpapers = [os.path.join(wallpaper_folder, file) 
              for file in os.listdir(wallpaper_folder) 
              if os.path.splitext(file)[1].lower() in image_extensions]

# Verificar que se hayan encontrado imágenes
if len(wallpapers) < 2:
    raise Exception("Necesitas al menos 2 imágenes en la carpeta para hacer la transición.")

# Barajar las imágenes para seleccionarlas de manera aleatoria
random.shuffle(wallpapers)

# Generar el contenido del archivo XML
xml_content = '''<background>
<starttime>
<year>2024</year>
<month>10</month>
<day>03</day>
<hour>00</hour>
<minute>00</minute>
<second>00</second>
</starttime>
'''

# Agregar imágenes y transiciones de forma aleatoria
for i in range(len(wallpapers)):
    next_index = (i + 1) % len(wallpapers)  # La siguiente imagen (si es la última, vuelve al inicio)
    
    xml_content += f'''
    <static>
        <duration>{static_duration}</duration>
        <file>{wallpapers[i]}</file>
    </static>
    <transition>
        <duration>{transition_duration}</duration>
        <from>{wallpapers[i]}</from>
        <to>{wallpapers[next_index]}</to>
    </transition>
    '''

xml_content += '</background>'

# Guardar el archivo XML
with open('/home/ricardo/noble.xml', 'w') as f:
    f.write(xml_content)

print("XML generado correctamente.")
