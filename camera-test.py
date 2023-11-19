from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
# camera_config = picam2.create_preview_configuration()
# picam2.configure(camera_config)
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})) #configura la videocamera
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(10)
