from PIL import Image

def mask_red_pixels(image_path):
    img = Image.open(image_path)
    pixels = img.getdata()
    masked_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        if r > g and r > b:  # If the pixel is red (red component is the highest)
            masked_pixels.append((255, 255, 255))  # White color (red pixel)
        else:
            masked_pixels.append((0, 0, 0))  # Black color (other pixels)

    masked_img = Image.new("RGB", img.size)
    masked_img.putdata(masked_pixels)

    result_image_path = image_path.replace("sample.png", "result.png")
    masked_img.save(result_image_path)

if __name__ == "__main__":
    image_path = "gw_test/Question2/sample.png"
    mask_red_pixels(image_path)
