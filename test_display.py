import cv2
import numpy as np

print("--- Script de diagnóstico de pantalla ---")
print("Este script no usa la cámara, solo intenta mostrar una imagen.")

# Crear una imagen negra de 500x500 píxeles
width, height = 500, 500
black_image = np.zeros((height, width, 3), dtype=np.uint8)

# Poner un texto en la imagen para que no esté vacía
cv2.putText(black_image, 'Si ves esto, funciona!', (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

window_name = 'Test Pantalla'

try:
    # Mostrar la imagen en una ventana
    cv2.imshow(window_name, black_image)
    print(f"Ventana '{window_name}' debería estar visible.")
    print("Presiona cualquier tecla para cerrar la ventana.")

    # Bucle continuo para forzar el redibujado de la ventana
    while True:
        key = cv2.waitKey(1) & 0xFF
        # Salir si se presiona cualquier tecla o si la ventana se cierra
        if key != 255 or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

except Exception as e:
    print(f"Error al intentar mostrar la ventana: {e}")

finally:
    # Cerrar todas las ventanas
    print("Cerrando ventanas.")
    cv2.destroyAllWindows()
