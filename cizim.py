import cv2
import turtle

# ================= FOTOĞRAF =================
img_path = "foto.jpg"

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("foto.jpg bulunamadı!")

# Kenar algılama
edges = cv2.Canny(img, 40, 120)
h, w = edges.shape

# ================= TURTLE =================
screen = turtle.Screen()
screen.bgcolor("white")

SCREEN_W, SCREEN_H = 900, 900
screen.setup(SCREEN_W, SCREEN_H)

t = turtle.Turtle()
t.hideturtle()
t.color("black")
t.pensize(2)
t.penup()

# 🔥 ANİMASYONU KAPAT (direkt çizim için)
screen.tracer(0, 0)

# ================= OTOMATİK ÖLÇEK =================
scale_x = (SCREEN_W - 40) / w
scale_y = (SCREEN_H - 40) / h
scale = min(scale_x, scale_y)

step = 1   # 1 = çok detaylı | 2 = daha hızlı

# Ortala
x_offset = - (w * scale) / 2
y_offset =   (h * scale) / 2

# ================= ÇİZİM =================
for y in range(0, h, step):
    drawing = False
    for x in range(0, w, step):
        if edges[y, x] > 0:
            px = x * scale + x_offset
            py = -y * scale + y_offset

            if not drawing:
                t.penup()
                t.goto(px, py)
                t.pendown()
                drawing = True
            else:
                t.goto(px, py)
        else:
            drawing = False
            t.penup()

# 🔥 TEK SEFERDE GÖSTER
screen.update()
turtle.done()
