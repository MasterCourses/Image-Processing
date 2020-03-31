# Implement Dithering
from PIL import Image
import numpy as np

# Input a grayscale image I
I = Image.open("my_cat.png").convert('L')
width, height = I.size

# Step1 : Define dithering matrix(D1) and generate dithering array(D)
# Define Dithering Matrix (2X2)
D1 = np.array([[0, 128],
              [192, 64]])

# Generate Dithering Array D of image size by repeating D2
D = np.tile(D1, (int(width/2), int(height/2)))

# Step2 : Threshold image I
for y in range(I.size[1]):      # y = height
    for x in range(I.size[0]):  # x = width

        ori_pixel = I.getpixel((x, y))

        # threshold and update pixel val.
        if ori_pixel > D[y][x]:
            I.putpixel((x, y), 255 * 1)
        else:
            I.putpixel((x, y), 0)

# Save new image I'
I.save("D1.png")

# Step3 : Show images ori_img(I) and dithering_img(D1)
I = Image.open("my_cat.png").convert('L')
I.show()
dithering_img = Image.open("D1.png")
dithering_img.show()
