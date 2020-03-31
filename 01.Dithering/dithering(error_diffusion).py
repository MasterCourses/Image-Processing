# Implement Error Diffusion Dithering
# Spread the error according to "Floyd-Steinberg"
from PIL import Image

# Input a grayscale image I
I = Image.open("my_cat.png").convert('L')
Width, Height = I.size

for y in range(Height):      # y = Height (Column)
    for x in range(Width):   # x = Width (Row)
        # Get each pixel I(x,y)
        ori_pixel = I.getpixel((x, y))

        # Step1 : Calculate Quantization Error
        if ori_pixel < 128:
            E = ori_pixel
        else:
            E = ori_pixel-255

        # Step2 : Spread the error according to "Floyd-Steinberg"
        if x < Width - 1:
            new_pixel = I.getpixel((x + 1, y)) + round(E * 7/16)
            if new_pixel > 255: new_pixel = 255
            elif new_pixel < 0: new_pixel = 0
            I.putpixel((x + 1, y), new_pixel)
        if y < Height - 1:
            new_pixel = I.getpixel((x, y + 1)) + round(E * 5/16)
            if new_pixel > 255: new_pixel = 255
            elif new_pixel < 0: new_pixel = 0
            I.putpixel((x, y + 1), new_pixel)
        if x < Width - 1 and y < Height - 1:
            new_pixel = I.getpixel((x + 1, y + 1)) + round(E * 1/16)
            if new_pixel > 255: new_pixel = 255
            elif new_pixel < 0: new_pixel = 0
            I.putpixel((x + 1, y + 1), new_pixel)
        if x > 0 and y < Height - 1:
            new_pixel = I.getpixel((x - 1, y + 1)) + round(E * 3/16)
            if new_pixel > 255 : new_pixel = 255
            elif new_pixel < 0 : new_pixel = 0
            I.putpixel((x - 1, y + 1), new_pixel)

        # Step3 : Quantize new I(x,y) to 0 or 255 (threshold)
        if ori_pixel < 128:
            I.putpixel((x, y), 0)  # threshold : 0
        else:
            I.putpixel((x, y), 255)  # threshold : 255

# -- Experimental results -- #
# Save new image
I.save("Floyd-Steinberg.png")
# Show images I and new image(use error diffusion dithering)
I = Image.open("my_cat.png").convert("L")
I.show()
dithering_img = Image.open("Floyd-Steinberg.png")
dithering_img.show()
