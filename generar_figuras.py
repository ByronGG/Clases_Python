import numpy as np
import cv2
import os
import random

SIZE = 128
DATASET = "shapes_dataset"
CLASSES = ["circle", "square", "triangle"]

def noise(img):
    n = np.random.randint(0, 40, (SIZE, SIZE, 3), dtype="uint8")
    return cv2.add(img, n)

def make_circle():
    img = np.zeros((SIZE, SIZE, 3), dtype="uint8")
    r = random.randint(20, 45)
    x = random.randint(r, SIZE-r)
    y = random.randint(r, SIZE-r)
    cv2.circle(img, (x, y), r, (255, 255, 255), -1)
    return noise(img)

def make_square():
    img = np.zeros((SIZE, SIZE, 3), dtype="uint8")
    s = random.randint(40, 70)
    x = random.randint(0, SIZE-s)
    y = random.randint(0, SIZE-s)
    cv2.rectangle(img, (x, y),(x+s, y+s), (255,255,255), -1)
    return noise(img)

def make_triangle():
    img = np.zeros((SIZE, SIZE, 3), dtype="uint8")
    pts = np.array([
        [random.randint(10, 118), random.randint(10, 118)],
        [random.randint(10, 118), random.randint(10, 118)],
        [random.randint(10, 118), random.randint(10, 118)],
    ])
    cv2.drawContours(img,[pts],0,(255,255,255), -1)
    return noise(img)

generators = {
    "circle": make_circle,
    "square": make_square,
    "triangle": make_triangle
}

for split in ["train", "val", "test"]:
    for c in CLASSES:
        os.makedirs(f"{DATASET}/{split}/{c}", exist_ok=True)

def create_images(split, n):
    for c in CLASSES:
        for i in range(n):
            img = generators[c]()
            cv2.imwrite(f"{DATASET}/{split}/{c}/{i}.png", img)

create_images("train", 400)
create_images("val", 100)
create_images("test", 100)

print("DATASET CREADO!!!")