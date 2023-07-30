from PIL import Image #, ImageChops

def crop_foreground(foreground_path, mask_path):
    foreground = Image.open(foreground_path)
    mask = Image.open(mask_path)
    mask = mask.convert("L")                                    # 1.Convert to grayscale
    mask = mask.point(lambda x: 255 if x < 128 else 0, '1')     # 2.Threshold to create a binary mask
    # inverted_mask = ImageChops.invert(mask)   if you want to invert the result.
    cropped_foreground = Image.new("RGBA", foreground.size)     # 3.New 'RGBA' image mode for the cropped foreground.
    cropped_foreground.paste(foreground, (0, 0), mask)          # 4.Apply the binary mask to the foreground
    return cropped_foreground
  
def composite_images(background_path, cropped_foreground, output_path):
    background = Image.open(background_path)
    cropped_foreground = cropped_foreground.resize(background.size, Image.LANCZOS)  # 1.Resize
    result = Image.alpha_composite(background.convert("RGBA"), cropped_foreground)  # 2.Composite
    result = result.convert("RGB")                                                  # 3.Reconvert to RGB mode to save as JPEG
    result.save(output_path, "JPEG")                                                # 4.Save the image

if __name__ == "__main__":
    background_path = "gw_test/Question2/background.jpg"
    foreground_path = "gw_test/Question2/foreground.jpg"
    mask_path = "gw_test/Question2/mask.png"
    output_path = "gw_test/Question2/result3.jpg"

    cropped_foreground = crop_foreground(foreground_path, mask_path)
    composite_images(background_path, cropped_foreground, output_path)
