import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    n = np.size(x)

    m_x = np.mean(x)
    m_y = np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    m = SS_xy / SS_xx
    c = m_y - m * m_x

    return (c, m)

def plot_regression_line(x, y, b):
    plt.scatter(x, y, color="m", marker="o", s=30)

    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="g")

    plt.xlabel('x')
    plt.ylabel('y')

def predict(x, b):
    y_pred = b[0] + b[1] * x
    return y_pred

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    b = estimate_coef(x, y)
    plot_regression_line(x, y, b)

    x_to_predict = 11
    y_predicted = predict(x_to_predict, b)
    print(f'For x={x_to_predict}, predicted y={y_predicted}')

    plt.show()

main()
