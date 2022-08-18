import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Example 1: constant variance
ts1 = []
mu, sigma, seg = 0.0, 1.0, 1000
for i in range(10):
    ts = np.random.normal(mu, sigma, seg) + np.random.randint(low=-10, high=10)
    ts1 = np.append(ts1, ts, axis=0)

plt.figure(figsize=(16, 4))
plt.plot(ts1)
plt.title("Example 1: Constant variance")

# Example 2: varying variance
ts2 = []
mu, sigma, seg = 0.0, 1.0, 1000
for i in range(10):
    sig = np.random.randint(low=1, high=50)
    ts = np.random.normal(mu, sigma * sig, seg)
    ts2 = np.append(ts2, ts, axis=0)

plt.figure(figsize=(16, 4))
plt.plot(ts2)
plt.title("Example 2: varying variance")

# Stacking subplots
fig, axs = plt.subplots(2)
plt.figure(figsize=(16, 4))
fig.suptitle('Varying/Constant Variance')
axs[0].plot(ts1)
axs[1].plot(ts2)
plt.show()