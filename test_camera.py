import cv2
import time

print("--- Script de diagnóstico de cámara v2 ---")

# Paso 1: Crear una ventana explícitamente
window_name = 'Test Cámara'
try:
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    print(f"Paso 1: Ventana '{window_name}' creada con éxito.")
    # Pequeña pausa para que el SO procese la creación de la ventana
    cv2.waitKey(100)
except Exception as e:
    print(f"Error en el Paso 1 al crear la ventana: {e}")
    exit()

# Paso 2: Intentar abrir la cámara
print("\nPaso 2: Intentando abrir la cámara (índice 0)...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error en el Paso 2: No se pudo abrir la cámara.")
    print("Asegúrate de que no esté en uso y de que la app tiene permisos en 'Ajustes del Sistema > Privacidad y seguridad > Cámara'.")
    exit()

print("Cámara abierta con éxito.")
print("\nPaso 3: Mostrando video. Presiona 'q' en la ventana para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el fotograma.")
        break

    # Mostrar el fotograma
    cv2.imshow(window_name, frame)

    # La llamada a waitKey es crucial para que la ventana se dibuje
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Tecla 'q' presionada. Saliendo...")
        break

print("\nCerrando todo.")
cap.release()
cv2.destroyAllWindows()
