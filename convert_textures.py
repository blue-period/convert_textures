from PIL import Image
import numpy as np
from pathlib import Path

class ConvertTextures:
    def __init__(self, input_image_path: Path):
        self.input_image_path = input_image_path 

        self.green_output_path = (self.input_image_path.parent / (str(self.input_image_path.stem) + "_green")).with_suffix(self.input_image_path.suffix)
        self.alpha_output_path = (self.input_image_path.parent / (str(self.input_image_path.stem) + "_alpha")).with_suffix(self.input_image_path.suffix)

    def green_normal_texture(self):
        # Open the PNG image
        img = Image.open(self.input_image_path).convert('RGBA')  # Ensure it's RGBA format
        img_array = np.array(img)
        red_channel = img_array[:, :, 0]
        green_channel = img_array[:, :, 1]
        blue_channel = img_array[:, :, 2]
        alpha_channel = img_array[:, :, 3]
        normal_green_channel = green_channel  # or any modification you prefer
        red_channel[:] = 0
        blue_channel[:] = 0 
        new_img_array = np.stack((red_channel, normal_green_channel, blue_channel, alpha_channel), axis=-1)
        new_img = Image.fromarray(new_img_array)
        new_img.save(self.green_output_path)


    def red_alpha_texture(self):
        img = Image.open(self.input_image_path).convert("L")  # Convert to grayscale
        img_array = np.array(img)
        new_img_array = np.zeros((img_array.shape[0], img_array.shape[1], 3), dtype=np.uint8)
        new_img_array[img_array == 255] = [255, 0, 0]  # White becomes Red (opaque)
        new_img_array[img_array == 0] = [0, 0, 0]      # Black stays black (transparent)
        new_img = Image.fromarray(new_img_array)
        new_img.save(self.alpha_output_path)


input = Path("./DefaultMaterial_Normal.png")
# Example usage

