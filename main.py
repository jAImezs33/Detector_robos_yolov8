# main.py

import cv2
from ultralytics import YOLO
import time
import os
import asyncio
from datetime import datetime

from telegram_bot import send_telegram_alert
from config import VIDEO_SOURCE, CONFIDENCE_THRESHOLD, NOTIFICATION_COOLDOWN

# Variable to track the last notification time
last_notification_time = 0

def main():
    global last_notification_time

    # Create a directory to save captures if it doesn't exist
    if not os.path.exists('captures'):
        os.makedirs('captures')

    # Load the custom YOLOv8 model
    try:
        model = YOLO("models/shoplifting_weights.pt")
    except Exception as e:
        print(f"Error al cargar el modelo YOLO: {e}")
        return

    # Open the video source
    cap = cv2.VideoCapture(VIDEO_SOURCE)

    if not cap.isOpened():
        print(f"Error: No se pudo abrir la fuente de video: {VIDEO_SOURCE}")
        return

    # Camera warm-up
    for _ in range(30):
        success, _ = cap.read()
        if success:
            break
        time.sleep(0.1)

    print("Detector de hurtos iniciado. Presiona Ctrl+C para detener.")

    while True:
        success, frame = cap.read()
        if not success:
            print("Se ha perdido la conexión con la cámara. Saliendo...")
            break

        # Run YOLOv8 inference on the frame
        results = model(frame, verbose=False)

        shoplifting_detected = False
        for r in results:
            for box in r.boxes:
                if box.cls == 1 and box.conf >= CONFIDENCE_THRESHOLD:
                    shoplifting_detected = True
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    label = f'Posible Hurto {box.conf.item():.2f}'
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                elif box.cls == 0:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)

        # Check if a notification should be sent
        current_time = time.time()
        if shoplifting_detected and (current_time - last_notification_time > NOTIFICATION_COOLDOWN):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            capture_filename = f"captures/hurto_{timestamp}.jpg"
            cv2.imwrite(capture_filename, frame)
            
            try:
                alert_message = f"¡Posible hurto detectado! {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                asyncio.run(send_telegram_alert(alert_message, capture_filename))
                last_notification_time = current_time
            except Exception as e:
                print(f"Error al enviar la alerta por Telegram: {e}")

        # Save the latest frame for live preview
        cv2.imwrite("live_preview.jpg", frame)

        # Small delay to prevent high CPU usage
        time.sleep(0.01)

    # Release resources
    cap.release()
    print("Detector detenido.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado: {e}")
