from PIL import Image
import matplotlib.pyplot as plt

from utils.sam_rooftop import extract_rooftop_sam


# Load rooftop image
img = Image.open("CV Raman.png").convert("RGB")


# Run hybrid SAM analysis
mask, area = extract_rooftop_sam(img)


# Print area
print("Usable Area:", area)


# Show mask
plt.figure(figsize=(8, 8))
plt.imshow(mask)
plt.title("Hybrid SAM Rooftop Mask")
plt.axis("off")
plt.show()