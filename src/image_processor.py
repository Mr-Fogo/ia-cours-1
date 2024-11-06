import os
from datetime import datetime

from PIL import Image, ImageOps


class ImageProcessor:

    def __init__(self, path):
        self.path = path

    def process_folder(self, size: int):
        """
        Process folder
        Args:
            size (int): size of new image
        """
        output_folder = os.path.join(
            "datasets", datetime.now().strftime("%Y%m%d%H%M%S")
        )
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(self.path):
            self.process_image(
                os.path.join(self.path, filename), size, output_folder
            )

    def process_image(self, filepath: str, size: int, output_folder: str):
        """
        Process image
        Args:
            filepath (str): Path to the image
            size (int): Size of the new image
            output_folder (str): Folder to save the processed image
        """
        try:
            img = Image.open(filepath)
            img = self.resize_and_pad(img, size)
            img.save(os.path.join(output_folder, os.path.basename(filepath)))
            img.close()

        except Exception as e:
            print(f"Error processing {filepath}: {e}")

    def resize_and_pad(self, img, size):
        """
        Resize and add padding
        Args:
            img: Image object
            size: target size for resizing
        """
        original_width = img.size[0]
        original_height = img.size[1]
        aspect_ratio = original_width / original_height

        if original_width > original_height:
            new_width = size
            new_height = int(size / aspect_ratio)
        else:
            new_height = size
            new_width = int(size * aspect_ratio)

        img = img.resize((new_width, new_height))

        delta_w = size - new_width
        delta_h = size - new_height
        padding = (0, 0, delta_w, delta_h)

        fill_color = (114, 114, 144) if img.mode == "RGB" else 114
        return ImageOps.expand(img, padding, fill=fill_color)
