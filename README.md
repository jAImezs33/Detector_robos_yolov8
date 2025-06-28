# Detector de Robos con YOLOv8 y Telegram

Este proyecto utiliza el modelo de detección de objetos YOLOv8 para identificar personas en una transmisión de video (como una cámara CCTV) y envía una alerta con una captura de pantalla a un chat de Telegram.

## Características

- Detección de personas en tiempo real usando YOLOv8.
- Notificaciones automáticas a Telegram con imagen.
- Configurable para diferentes fuentes de video (webcam, archivo de video, stream RTSP).
- Cooldown para evitar el envío masivo de notificaciones.

## Requisitos

- Python 3.8 o superior
- Una cámara de video o un archivo de video para analizar.
- Un bot de Telegram y el ID de un chat.

## Instalación

1.  **Clona o descarga este repositorio.**

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1.  **Crea un bot de Telegram:**
    -   Habla con [@BotFather](https://t.me/BotFather) en Telegram.
    -   Usa el comando `/newbot` para crear un nuevo bot.
    -   BotFather te dará un **token**. Cópialo.

2.  **Obtén tu Chat ID de Telegram:**
    -   Habla con tu nuevo bot y envíale cualquier mensaje.
    -   Luego, abre tu navegador y ve a la siguiente URL, reemplazando `YOUR_TELEGRAM_BOT_TOKEN` con tu token:
        `https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/getUpdates`
    -   Busca el objeto `chat` y copia el valor del campo `id`. Ese es tu **Chat ID**.

3.  **Edita el archivo `config.py`:**
    -   Pega tu token en la variable `TELEGRAM_TOKEN`.
    -   Pega tu Chat ID en la variable `TELEGRAM_CHAT_ID`.
    -   Ajusta `VIDEO_SOURCE` a tu fuente de video (`0` para la webcam por defecto, la ruta a un archivo, o una URL RTSP).

## Uso

Una vez configurado, ejecuta el script principal desde tu terminal:

```bash
python main.py
```

El script comenzará a analizar el video. Cuando detecte a una persona, guardará una imagen en la carpeta `captures` y enviará una alerta a tu chat de Telegram.

Para detener el detector, presiona la tecla `q` en la ventana de video (si está visible) o `Ctrl+C` en la terminal.

## Personalización

-   **Modelo YOLO:** Puedes usar otros modelos de YOLOv8 (ej. `yolov8s.pt`, `yolov8m.pt`) cambiando el nombre en `main.py`. Modelos más grandes son más precisos pero más lentos.
-   **Lógica de Detección:** La lógica actual alerta al detectar cualquier persona. Puedes modificar `main.py` para implementar reglas más complejas, como detectar personas en áreas específicas del video (Regions of Interest - ROI).
