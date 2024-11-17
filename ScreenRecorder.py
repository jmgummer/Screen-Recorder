import cv2
import numpy as np
import pyautogui

screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

name = input("Kindly Name Your Output File: ")
fps = int(input("Set frames per second(FPS) recommended 30: "))
recording_duration = int(input("Set recording duration(seconds): "))
output_filename = name + ".mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_filename, fourcc, fps, resolution)

print("Starting To Capture "+ output_filename)
for _ in range(int(recording_duration * fps)):
    screen = pyautogui.screenshot()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

out.release()