# Implement Histogram Equalization program to gray image

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Input a grayscale image
gray_img = Image.open('my_cat(low_contrast).png').convert("L")
L = 256  # 8 bits grayscale

# Define 8 bits grayscale value into an array
gray_scale = gray_img.histogram()   # nk : Number of pixels in each grayscale(n0~n255)

# Calculate total pixels
Width, Height = gray_img.size  # Size: 244 * 244
N = Width * Height             # N = Total pixels = 59536

# Save original gray_img histogram
a = np.array(gray_img)
plt.hist(a.ravel(), bins=L)  # ravel(): Return a contiguous flattened array , bins: number of pixels
plt.ylabel('Number of pixels')
plt.xlabel('Gray Scale')
plt.savefig('input_hist.png')  # Save input_img histogram
plt.show()

# HISTOGRAM EQUALIZATION (HE) to gray
# Step1 : Calculate PMF and CDF
PMF = [0] * 256     # initial zero value in PMF[0] ~ PMF[256]
CDF = [0] * 256     # initial zero value in CDF[0] ~ CDF[256]
sum = 0             # initial cummulative_probability
for r in range(256):
    PMF[r] = gray_scale[r] / N      # Calculate Probability mass function(PMF)
    sum += PMF[r]
    CDF[r] = sum                    # Calculate Cumulative distribution function(CDF)

# Step2: s=T(r) , T(r): transformation function
for y in range(Height):
    for x in range(Width):
       ori_pixel = gray_img.getpixel((x, y))
       gray_img.putpixel((x, y), round((L-1) * CDF[ori_pixel]))

# Save output_img histogram
gray_img.save('HE(Gray)_result.png')
a = np.array(gray_img)
plt.hist(a.ravel(), bins=L, color='darkorange')
plt.ylabel('Number of pixels')
plt.xlabel('Gray Scale')
plt.savefig('output_hist.png')  # Save output_img histogram
plt.show()
