# HW5-a (Implement unsharp masking and use average filter)

from PIL import Image, ImageDraw

# Input a color image (RGB
input_image = Image.open("W.E.Hill.png").convert("RGB")
input_pixels = input_image.load()

# (low-pass) Average Filter mask
mask = [[1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9],
        [1 / 9, 1 / 9, 1 / 9]]
k = 0.9
val = 9  # scale for display

# Middle of the kernel
offset = len(mask) // 2

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

for y in range(offset, input_image.height - offset):
    for x in range(offset, input_image.width - offset):
        original_pixel = input_pixels[x, y]
        acc = [0, 0, 0]

        # Compute convolution between intensity and mask
        for a in range(len(mask)):
            for b in range(len(mask)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] += pixel[0] * mask[a][b]
                acc[1] += pixel[1] * mask[a][b]
                acc[2] += pixel[2] * mask[a][b]

        # Unsharp masking
        new_pixel = (
            int(original_pixel[0] - acc[0] * k) * val,
            int(original_pixel[1] - acc[1] * k) * val,
            int(original_pixel[2] - acc[2] * k) * val
        )
        draw.point((x, y), new_pixel)

# Save experimental image
output_image.save("unsharp(average filter).png")

