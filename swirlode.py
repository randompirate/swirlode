import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np

pi = np.pi
sqrt = np.sqrt
cos = np.cos
sin = np.sin

def deriv_z(z,t):
    x, xdot, y, ydot = z
    return [xdot, -2*y*ydot*t**3,
            ydot, -y-.01*ydot]


t = np.linspace(0, 100, 5000)

# plt.plot(t, x)
fig, ax = plt.subplots()

plt.grid(False)
plt.axis('off')


for s in range(4):
  s = s/40

  z_init = [0, 0.5*cos(pi/3 + s)+5*s,
            0, 0.5*sin(pi/3 + s)]

  z = integrate.odeint(deriv_z, z_init, t)

  x, xdot, y, ydot = z.T

  # ax.plot(t, x)
  # ax.plot(t, y)
  ax.plot(x,y)

  if s == 0:
    plt.savefig('swirl.png')


plt.savefig('swirl4.png')
# plt.show()