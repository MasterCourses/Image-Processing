# Implement Dithering extend to n=8 gray values
from PIL import Image
import numpy as np

# Input a grayscale image I
I = Image.open("my_cat.png").convert('L')
width, height = I.size

# Step1 : n output and m range Declaration
n = 8
m = int(255/(n-1))

# Step2 : Define and Calculate Q
column = height
row = width
# Define Q (2D Array)
Q = [[0 for _ in range(row)] for _ in range(column)]
# Calculate Q(i,j) value
for j in range(I.size[1]):      # j = column
    for i in range(I.size[0]):  # i = row
        Q[j][i] = int(I.getpixel((i, j))/m)  # Q(i,j) = [I(i,j)/85]

# Step3 :Define dithering matrix(D1) and generate dithering array(D)
# Define Dithering Matrix (2X2)
D1 = np.array([[0, 24],
              [36, 12]])

# Generate Dithering Array D of image size by repeating D1
D = np.tile(D1, (int(width/2), int(height/2)))

# Step4 : Threshold image I
for j in range(I.size[1]):      # j = column
    for i in range(I.size[0]):  # i = row

        ori_pixel = I.getpixel((i, j))

        if ori_pixel - m * Q[j][i] > D[j][i]:
            I.putpixel((i, j), m * (Q[j][i] + 1))
        else:
            I.putpixel((i, j), m * (Q[j][i] + 0))

# Save new image I'
I.save("D8.png")

# Step5 : Display images I and I'(dithering_img)
I = Image.open("my_cat.png").convert('L')
I.show()
dithering_img = Image.open("D8.png")
dithering_img.show()

