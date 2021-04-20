from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from termcolor import colored
import face_recognition
from sys import exit
import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-f', required=True, type=str, help='Sua fotinha')
parser.add_argument('-o', required=False, default="juju1.png", type=str, help='Sua JuJu')
args = vars(parser.parse_args())

file_fotinha = args['f']
juju = Image.open(args['o'])

fotinha = face_recognition.load_image_file(file_fotinha)
face_landmarks_list = face_recognition.face_landmarks(fotinha)

if len(face_landmarks_list) == 0:
	print(colored('\033[1m'+"\n - Vish, não consegui identificar seus olhos :/\n", "red"))
	exit(0)

new_fotinha = Image.open(file_fotinha)

for detail, points in face_landmarks_list[0].items():
    if detail == "left_eyebrow":
        x1_oculos = points[0][0]
        position = (points[0][0]+3, points[0][1]-5)
        altura_oculos = min(points, key=lambda x: x[1])[1]
    if detail == "right_eyebrow":
        x2_oculos = points[-1][0]
    if detail == "left_eye":
        altura_oculos = np.abs(altura_oculos - max(points, key=lambda x: x[1])[1])

juju = juju.resize((x2_oculos - x1_oculos, altura_oculos))
foreground = juju

new_fotinha.paste(juju, position, foreground)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

new_fotinha.save("geral_de_juju/eu_de_juju_"+str(current_time)+".png")
print(colored('\033[1m'+"\n - Agora você está de Juju 8-): "+" geral_de_juju/eu_de_juju_"+str(current_time)+".png", "blue"))