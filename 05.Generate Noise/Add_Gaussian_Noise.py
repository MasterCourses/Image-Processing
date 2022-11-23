# HW9-method1 (Generation of zero mean Gaussian noise)

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Create an image g and the same gray values of 100
g = Image.open("g.png").convert("L")
for i in range(g.size[0]):
    for j in range(g.size[1]):
        g.putpixel((i, j), 100)

g.save("g.png")
g.show()

# Save image g histogram
a = np.array(g)
plt.hist(a.ravel(), bins=256)
plt.ylabel('Number of pixels')
plt.xlabel('Gray Scale')
plt.savefig('g_histogram.png')
plt.show()

# 2. Generate Gaussian noise n and Show noisy image f
# Calculate Gaussian noise with menu=0 and variance=15
menu = 0
variance = 15
noise = np.random.normal(menu, variance, g.size)
# Add the noise to the image g
f_array_noise = np.add(np.array(g), noise) # f = g + noise
f = Image.fromarray(f_array_noise)
# Show the noisy image f
f.show()

# 3. Save and display noisy image f histogram
a = np.array(f)
plt.hist(a.ravel(), bins=256)
plt.ylabel('Number of pixels')
plt.xlabel('Gray Scale')
plt.savefig('f_histogram.png')
plt.show()