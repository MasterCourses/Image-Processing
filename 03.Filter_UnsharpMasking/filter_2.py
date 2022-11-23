# HW5-b (Implement unsharp masking and use median filter)

from PIL import Image, ImageFilter

# Input a color image (RGB)
input_image = Image.open("W.E.Hill.png").convert("RGB")
width, height = input_image.size

# Using Median filter (3X3)
filter_image = input_image.filter(ImageFilter.MedianFilter(3))

# Unsharp masking
k = 0.9
val = 9  # scale for display
for y in range(height):
    for x in range(width):
        original_pixel = input_image.getpixel((x, y))
        filter_pixel = filter_image.getpixel((x, y))
        new_pixel = (
            int(original_pixel[0] - filter_pixel[0] * k) * val,
            int(original_pixel[1] - filter_pixel[1] * k) * val,
            int(original_pixel[2] - filter_pixel[2] * k) * val
        )
        input_image.putpixel((x,y), new_pixel)

# Save experimental image
input_image.save("unsharp(median filter).png")



