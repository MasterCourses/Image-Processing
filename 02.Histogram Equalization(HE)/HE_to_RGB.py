# Implement Histogram Equalization program to color image

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Input a color image (RGB)
color_img = Image.open('my_cat(RGB_low_contrast).png').convert('RGB')
L = 256

# Define RGB value into an array
color_scale = color_img.histogram()
color_scale_R = color_scale[0:256]      # nk : Number of pixels in each Red pixels(n0~n255)
color_scale_G = color_scale[256:513]    # nk : Number of pixels in each green pixels(n256~n512)
color_scale_B = color_scale[512:769]     # nk : Number of pixels in each blue pixels(n512~n768)

# Calculate total pixels
Width, Height = color_img.size  # Size: 244 * 244
N = Width * Height             # N = Total pixels = 59536

# Save original color_img histogram
a = np.array(color_img)

# Red Histogram
plt.hist(a[:, :, 0].ravel(), bins=256, color='red')
plt.ylabel('Number of pixels')
plt.xlabel('RGB (Red pixels)')
plt.savefig('input_red_hist.png')  # Save input_img histogram
plt.close()

# Green Histogram
plt.hist(a[:, :, 1].ravel(), bins=256, color='green')
plt.ylabel('Number of pixels')
plt.xlabel('RGB (Green pixels)')
plt.savefig('input_green_hist.png')  # Save input_img histogram
plt.close()

# Blue Histogram
plt.hist(a[:, :, 2].ravel(), bins=256, color='blue')
plt.ylabel('Number of pixels')
plt.xlabel('RGB (Blue pixels)')
plt.savefig('input_blue_hist.png')  # Save input_img histogram
plt.close()

# HISTOGRAM EQUALIZATION (HE) to color image
# initial zero value in PMF_RGB
PMF_R = [0] * 256
PMF_G = [0] * 256
PMF_B = [0] * 256
# initial zero value in CDF_RGB
CDF_R = [0] * 256
CDF_G = [0] * 256
CDF_B = [0] * 256
# initial cummulative_probability (RGB)
sum_R = 0
sum_G = 0
sum_B = 0

# Step1 : Calculate PMF and CDF
for i in range(256):
    PMF_R[i] = color_scale_R[i] / N      # Calculate Probability mass function(PMF_R)
    sum_R += PMF_R[i]
    CDF_R[i] = sum_R                     # Calculate Cumulative distribution function(CDF_R)

for i in range(256):
    PMF_G[i] = color_scale_G[i] / N      # Calculate Probability mass function(PMF_G)
    sum_G += PMF_G[i]
    CDF_G[i] = sum_G                     # Calculate Cumulative distribution function(CDF_G)

for i in range(256):
    PMF_B[i] = color_scale_B[i] / N      # Calculate Probability mass function(PMF_R)
    sum_B += PMF_B[i]
    CDF_B[i] = sum_B                     # Calculate Cumulative distribution function(CDF_G)

# Step2: s=T(r) , T(r): transformation function
for y in range(Height):
    for x in range(Width):
        r, g, b = color_img.getpixel((x, y))
        color_img.putpixel((x, y), (round((L - 1) * CDF_R[r]), round((L - 1) * CDF_G[g]), round((L - 1) * CDF_B[b])))

# Save output_img histogram
color_img.save('output_img.png')
a = np.array(color_img)

# Red Histogram
plt.hist(a[:, :, 0].ravel(), bins=256, color='red')
plt.ylabel('Number of pixels')
plt.xlabel('RGB (Red pixels)')
plt.savefig('output_red_hist.png')
plt.close()

# Green Histogram
plt.hist(a[:, :, 1].ravel(), bins=256, color='green')
plt.ylabel('Number of pixels')
plt.xlabel('RGB (Green pixels)')
plt.savefig('output_green_hist.png')
plt.close()

# Blue Histogram
plt.hist(a[:, :, 2].ravel(), bins=256, color='blue')
plt.ylabel('Number of pixels')
plt.xlabel('RGB (Blue pixels)')
plt.savefig('output_blue_hist.png')
plt.close()