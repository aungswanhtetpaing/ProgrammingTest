from PIL import Image

def crop_foreground(foreground_path, mask_path):
    foreground = Image.open(foreground_path)
    mask = Image.open(mask_path)

    mask = mask.convert("L")                                    # Convert to grayscale
    mask = mask.point(lambda x: 255 if x < 128 else 0, '1')     # Threshold to create binary mask

    # inverted_mask = ImageChops.invert(mask)   if you want to invert the result.

    cropped_foreground = Image.new("RGBA", foreground.size)     # New 'RGBA' image mode for cropped foreground.
    cropped_foreground.paste(foreground, (0, 0), mask)          # Apply the binary mask to the foreground

    return cropped_foreground

def composite_images(background_path, cropped_foreground, output_path):
    background = Image.open(background_path)

    cropped_foreground = cropped_foreground.resize(background.size, Image.LANCZOS)  # Resize
    result = Image.alpha_composite(background.convert("RGBA"), cropped_foreground)  # Composite
    result = result.convert("RGB")                                                  # Reconvert to RGB mode to save as JPEG
    result.save(output_path, "JPEG")                                                # Save the image

def crop_center(image, size):
    width, height = image.size
    left = (width - size[0]) / 2
    top = (height - size[1]) / 2
    right = (width + size[0]) / 2
    bottom = (height + size[1]) / 2
    return image.crop((left, top, right, bottom))

def rotate_image(image, angle):
    return image.rotate(angle, resample=Image.BICUBIC, center=(image.width/2, image.height/2))

if __name__ == "__main__":
    background_path = "gw_test/Question2/background.jpg"
    foreground_path = "gw_test/Question2/foreground.jpg"
    mask_path = "gw_test/Question2/mask.png"
    output_path = "gw_test/Question2/result4.jpg"

    cropped_foreground = crop_foreground(foreground_path, mask_path)

    composite_images(background_path, cropped_foreground, "gw_test/Question2/result3.jpg")

    result_image = Image.open("gw_test/Question2/result3.jpg")      # 1.Open the image

    cropped_image = crop_center(result_image, (1024, 1024))         # 2.Crop the image to 1024x1024 with the center of gravity as the center

    rotated_image = rotate_image(cropped_image, -30)                # 3. Rotate the cropped image 30 degrees clockwise

    rotated_image.save(output_path, "JPEG")                         # 4.save
