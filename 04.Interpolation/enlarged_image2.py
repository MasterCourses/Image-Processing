# HW6-(ii) (Implement Image Enlargement & filling use Bilinear interpolation)

from PIL import Image
import numpy as np

# Step1 : Input a grayscale image I
I = Image.open("W.E.Hill.png").convert("L")
width, height = I.size
new_row = width * 2
new_column = height * 2

# Step2 : Zero interleave
enlarged_image = I
enlarged_image = enlarged_image.resize((new_row, new_column))
I2 = np.array(enlarged_image)
for j in range(I.size[0] * 2):
    for i in range(I.size[1] * 2):
        if (i % 2 == 0) and (j % 2 == 0):  # I:even
            I2[j][i] = I.getpixel((i / 2, j / 2))
        else:                             # I:odd
            I2[j][i] = 0

# Step3 : Filling(Bilinear interpolation)
Bilinear_mask = [[1, 2, 1],
                 [2, 4, 2],
                 [1, 2, 1]]
# Convolution I2 with NN interpolation
for j in range(len(I2[1])):
    for i in range(len(I2[0])):
        tmp = 0
        for b in range(len(Bilinear_mask)):
            for a in range(len(Bilinear_mask)):
                if (j+b-1 >= new_column) or (i+a-1 >= new_row):
                    tmp += 0 * Bilinear_mask[b][a]
                else:
                    tmp += I2[j+b-1][i+a-1] * Bilinear_mask[b][a]
        # reDraw image
        enlarged_image.putpixel((i, j), int(tmp/4))

# Step4 : Save and output enlarged images
enlarged_image.save("enlarged_image.png")
enlarged_image.show()
