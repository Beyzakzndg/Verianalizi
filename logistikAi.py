import numpy as np
import matplotlib.pyplot as plt
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

loss_history = []
for _ in range(epochs):
    z = X @ w                 # lineer düşünme
    y_hat = sigmoid(z)        # olasılık

    error = y - y_hat
    loss = np.mean(error ** 2)
    loss_history.append(loss)

    w = w + learning_rate * X.T @ error
plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Hata (MSE)")
plt.title("Sigmoid (Logistic) Öğrenme Süreci")
plt.grid(True)
plt.show()
new_student = np.array([[75, 70]]) / 100
probability = sigmoid(new_student @ w)

print("Olasılık:", probability[0, 0])

print("GEÇTİ" if probability > 0.5 else "KALDI")
