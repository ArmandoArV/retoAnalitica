import numpy as np
import matplotlib.pyplot as plt
from StatistaP import *

x=ChangeUSA
y=PriceUSA

def estim_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return (b_0, b_1)
 
def graph_reg(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    plt.plot(x, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
 
def main():
    # estimating coefficients
    b = estim_coef(x, y)
    print("Coeffs:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    graph_reg(x, y, b)
if __name__ == "__main__":
    main()