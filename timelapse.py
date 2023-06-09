#!/usr/bin/python3
import time
import glob
import os
import logging

from picamera2 import Picamera2
from systemd import journal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.addHandler(journal.JournaldLogHandler())

picam2 = Picamera2()
picam2.configure("still")
picam2.start()

list_of_files = glob.glob('/home/cam/timelapse/tomate/*.jpg')
latest_file = max(list_of_files, key=os.path.getmtime)
i = int(latest_file.split("-")[1].split(".")[0]) + 1

# Give time for Aec and Awb to settle.
time.sleep(10)

start_time = time.time()
while True:
    r = picam2.capture_request()
    r.save("main", f"/home/cam/timelapse/tomate/image-{i}.jpg")
    r.release()
    i += 1
    time.sleep(60)
    logger.info(f"Captured image {i} {time.time() - start_time:.2f}s since restart.")


picam2.stop()