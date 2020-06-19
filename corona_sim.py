import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
import copy
import kal_python as kal


sigma = 1.0/4.6
beta = 2.2
xi = 1.0/280
gamma = 1.0/5.0/4
delta = 0.001
h = 1 # 1サイクルあたりの日数
T = 90 # 日数
mu = 0
nu = 0
N = 10**9


def seirsd(x):
    S = x[0]
    E = x[1]
    I = x[2]
    R = x[3]
    D = N-S-E-I-R
    dS = mu * N - beta * S * I / N + xi * R - nu * S
    dE = beta * S * I / N - sigma * E - nu * E
    dI = sigma * E - gamma * I - nu * I -delta * I
    dR = gamma * I - xi * R
    dx = np.array([dS,dE,dI,dR])
    return dx


class function:    
    def update(self,t,x):
        dx = seirsd(x)
        return dx

x0 = np.array([[N-2],[0],[2],[0]]) # 初期条件
corona = function()
diff_eq = kal.differential_equation(4,corona,h,T,0,x0)
diff_eq.solve()

D = N - (diff_eq.x[0,:]+diff_eq.x[1,:]+diff_eq.x[2,:]+diff_eq.x[3,:])
x_fig = np.r_['0,2,-1',diff_eq.x,D]
fig = kal.t_x_plot(5,T)
fig.set_label(["S","E","I","R","D"])
fig.show(diff_eq.t,x_fig)
