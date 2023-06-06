import cv2
import time
from PIL import Image
from datetime import timedelta

# Crear un objeto de captura de video para acceder a la cámara
cam = cv2.VideoCapture(0)

# Verificar si la cámara está abierta correctamente
if not cam.isOpened():
    raise Exception("No se puede abrir la cámara")

# Obtener el tiempo actual
start_time = time.time()

# Duración total de la vista previa (en segundos)
preview_duration = 7

# Bucle para mostrar la vista previa de la cámara durante el tiempo especificado
while (time.time() - start_time) < preview_duration:
    # Calcular el tiempo restante
    remaining_time = preview_duration - (time.time() - start_time)
    remaining_time = max(0, remaining_time)  # Asegurar que el tiempo restante no sea negativo

    # Leer el fotograma actual de la cámara
    ret, frame = cam.read()

    # Mostrar el fotograma en una ventana llamada "Vista previa"
    cv2.imshow("Vista previa", frame)

    # Mostrar el tiempo restante en la ventana de la vista previa
    time_str = f"Tiempo restante: {timedelta(seconds=int(remaining_time))}"
    cv2.putText(frame, time_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255, 255), 2)
    cv2.imshow("Vista previa", frame)

    # Esperar 1 milisegundo para permitir que se actualice la ventana
    cv2.waitKey(1)

# Capturar una imagen después de la vista previa
ret, frame = cam.read()

new_width = 1230
new_height = 1711
resized_frame = cv2.resize(frame, (new_width, new_height))

# Guardar la imagen en un archivo
cv2.imwrite("imagen2.jpg", resized_frame)

# Abrir la imagen y realizar el proceso de superposición

img4 = cv2.imread(r"C:/Users/estudiante/Desktop/IMPORTANTE PYTHON/logoTecnica5.png")
img2 = Image.open(r"C:/Users/estudiante/Desktop/IMPORTANTE PYTHON/imagen2.jpg")
img1 = Image.open(r"C:/Users/estudiante/Desktop/IMPORTANTE PYTHON/marcoAzul.png")

img4 = cv2.resize(img4, (250,250))
cv2.imwrite("logoTecnica1.jpg", img4)
img4 = Image.open(r"C:/Users/estudiante/Desktop/IMPORTANTE PYTHON/logoTecnica1.jpg")

img1.paste(img2, (104, 104))

# Convertir la imagen resultante a modo RGB
img1_rgb = img1.convert("RGB")

# Guardar la imagen resultante en un archivo JPEG
img1_rgb.save("imagen_resultante.jpg")

img3 = Image.open(r"C:/Users/estudiante/Desktop/IMPORTANTE PYTHON/imagen_resultante.jpg")

img3.paste(img4,(1085, 1565))

# Mostrar la imagen resultante
img3.show()
