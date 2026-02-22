import math
import matplotlib.pyplot as plt
import numpy as np

# Your settings
INTERVAL = [-2*math.pi, 2*math.pi] # Expanded to show the origin clearly
N = 500 

def f(x):
    return math.sin(x)

x = np.linspace(INTERVAL[0], INTERVAL[1], N)
y = [f(i) for i in x]

fig, ax = plt.subplots(figsize=(8, 5))

# The "xOy" Magic
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Plotting
ax.plot(x, y, label='function', color='blue', linewidth=2)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

plt.show()