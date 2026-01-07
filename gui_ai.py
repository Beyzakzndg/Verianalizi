import numpy as np
import tkinter as tk
from tkinter import messagebox

# ===== Yapay Zeka Kısmı =====

X = np.array([
    [70, 80],
    [40, 50],
    [90, 90]
]) / 100

y = np.array([1, 0, 1]).reshape(-1, 1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

np.random.seed(0)
w = np.random.rand(2, 1)
learning_rate = 0.5
epochs = 1000

for _ in range(epochs):
    z = X @ w
    y_hat = sigmoid(z)
    error = y - y_hat
    w = w + learning_rate * X.T @ error

# ===== GUI Kısmı =====

def hesapla():
    try:
        vize = float(entry_vize.get())
        final = float(entry_final.get())
        
        yeni = np.array([[vize, final]]) / 100
        olasilik = sigmoid(yeni @ w)[0, 0]

        sonuc = "GEÇTİ ✅" if olasilik > 0.5 else "KALDI ❌"

        messagebox.showinfo(
            "Sonuç",
            f"Olasılık: {olasilik:.2f}\nSonuç: {sonuc}"
        )

    except:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar gir!")

# ===== Pencere =====

pencere = tk.Tk()
pencere.title("Yapay Zeka Not Tahmini")
pencere.geometry("300x220")
pencere.resizable(False, False)

tk.Label(pencere, text="Vize Notu").pack(pady=5)
entry_vize = tk.Entry(pencere)
entry_vize.pack()

tk.Label(pencere, text="Final Notu").pack(pady=5)
entry_final = tk.Entry(pencere)
entry_final.pack()

tk.Button(
    pencere,
    text="HESAPLA",
    command=hesapla,
    bg="#4CAF50",
    fg="white",
    width=15
).pack(pady=20)

pencere.mainloop()
