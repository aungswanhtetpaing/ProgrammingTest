from PIL import Image

def count_pixels_by_color(image_path):
    img = Image.open(image_path)
    pixels = img.getdata()
    pixel_counts = {}

    for pixel in pixels:
        r, g, b = pixel
        color = 'red' if r > g and r > b else 'green' if g > r and g > b else 'blue'
        pixel_counts[color] = pixel_counts.get(color, 0) + 1

    return pixel_counts

def print_pixel_counts(pixel_counts):
    print(f"red   : {pixel_counts.get('red', 0):6} pixels")
    print(f"green : {pixel_counts.get('green', 0):6} pixels")
    print(f"blue  : {pixel_counts.get('blue', 0):6} pixels")

if __name__ == "__main__":
    image_path = "gw_test/Question2/sample.png"
    pixel_counts = count_pixels_by_color(image_path)
    print_pixel_counts(pixel_counts)
