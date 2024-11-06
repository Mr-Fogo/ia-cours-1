import numpy as np
from PIL import Image

"""
image = Image.open("../images/dami.png")

resized_image = image.resize((300,300))

rotated_image = image.rotate(90)

rotated_image.save("update_image.png")

"""

image = Image.open("../../images/dami.png")
image_data = np.array(image)

print(image_data.shape)

new_array = np.array([[1, 2], [3, 4]])
print(new_array * 2)
sequence_data = np.arange(2, 14)
print(sequence_data)
sequence_data = sequence_data.reshape(6, 2)

image_data[:, :, 2] = 0
"""print(image_data)"""

processed_image = Image.fromarray(image_data)
processed_image.save("../image_after/processed_image.png")
print("toto")
