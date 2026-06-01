from rembg import remove # type: ignore
from PIL import Image # type: ignore

input_path = "image.png"
output_path = "output.png"

input_image = Image.open(input_path)
output_image = remove(input_image)

output_image.save(output_path)

print("Background eliminat!")