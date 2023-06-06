import cv2
import time

# Crear un objeto de captura de video para acceder a la cámara
cam = cv2.VideoCapture(0)

# Verificar si la cámara está abierta correctamente
if not cam.isOpened():
    raise Exception("No se puede abrir la cámara")

# Obtener el tiempo actual
start_time = time.time()

# Bucle para mostrar la vista previa de la cámara durante 7 segundos
while (time.time() - start_time) < 7:
    # Leer el fotograma actual de la cámara
    ret, frame = cam.read()

    # Mostrar el fotograma en una ventana llamada "Vista previa"
    cv2.imshow("Vista previa", frame)

    # Esperar 1 milisegundo para permitir que se actualice la ventana
    cv2.waitKey(1)

# Cerrar la ventana de vista previa y liberar la cámara
cv2.destroyAllWindows()
cam.release()
