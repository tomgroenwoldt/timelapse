ffmpeg -framerate 120 -i image-%d.jpg -c:v libx264 -r 60 timelapse.mp4
