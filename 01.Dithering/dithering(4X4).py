# Implement Dithering
from PIL import Image
import numpy as np

# Input a grayscale image I
I = Image.open("my_cat.png").convert('L')
width, height = I.size

# Step1 : Define dithering matrix(D1) and generate dithering array(D)
# Define Dithering Matrix (2X2)
D2 = np.array([[0, 128, 32, 160],
              [192, 64, 224, 96],
               [48, 176, 16, 144],
               [240, 112, 208, 80]])

# Generate Dithering Array D of image size by repeating D2
D = np.tile(D2, (int(width/4), int(height/4)))

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
I.save("D2.png")

# Step3 : Show images ori_img(I) and dithering_img(D1)
I = Image.open("my_cat.png").convert('L')
I.show()
dithering_img = Image.open("D2.png")
dithering_img.show()
