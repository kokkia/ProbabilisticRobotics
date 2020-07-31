
import numpy as np
import matplotlib.pyplot as plt
import kal_python as kal
# import figure
N = 1000 # 繰り返し回数
x_log = np.zeros(N)
y_log = np.zeros(N)
fig = kal.t_x_plot(1,N)
fig.set_txlabel("x0","x1")


class loss: # 損失関数の定義
  def update(self,x):
    y = (x[0,0]-1)**2 + x[1,0]**2 # [x0,x1]=[1,0]で最小となる関数
    return y

p = loss()
J = kal.Jacobian(p,2,1) # 上記ヤコビアンクラスのオブジェクト生成
x = np.array([-2,-2]).reshape(2,1) # 初期値
y = p.update(x)
print(y)
eta = 0.001 # 学習率

for i in range(N):
  x_log[i] = x[0]
  y_log[i] = x[1]
  j = J.update(x)
  x = x - eta * j.reshape(2,1) # 勾配法による更新
 
print(x)
print(p.update(x))

gm = kal.gradient_method(p, 2, 1)
print("optimizer:")
x_ = gm.solve(np.array([-2, 2]).reshape(2, 1))
print(x_)
plt.plot(x_log, y_log, '-o')
plt.show()